import json
import datetime
import os
import pymysql
import jwt
import time
from flask import Flask, request, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dbutils.pooled_db import PooledDB

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['OPENAPI_VERSION'] = '3.0.2'
app.url_map.strict_slashes = False


class MysqlClient(object):
    __pool = None

    def __init__(self, mincached=10, maxcached=20, maxshared=10, maxconnections=200, blocking=True,
                 maxusage=100, setsession=None, reset=True,
                 host='127.0.0.1', port=3306, db='forum',
                 user='root', passwd='123456', charset='utf8mb4'):
        """
        :param mincached:连接池中空闲连接的初始数量
        :param maxcached:连接池中空闲连接的最大数量
        :param maxshared:共享连接的最大数量
        :param maxconnections:创建连接池的最大数量
        :param blocking:超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
        :param maxusage:单个连接的最大重复使用次数
        :param setsession:optional list of SQL commands that may serve to prepare
            the session, e.g. ["set datestyle to ...", "set time zone ..."]
        :param reset:how connections should be reset when returned to the pool
            (False or None to rollback transcations started with begin(),
            True to always issue a rollback for safety's sake)
        :param host:数据库ip地址
        :param port:数据库端口
        :param db:库名
        :param user:用户名
        :param passwd:密码
        :param charset:字符编码
        """

        if not self.__pool:
            self.__class__.__pool = PooledDB(pymysql,
                                             mincached, maxcached,
                                             maxshared, maxconnections, blocking,
                                             maxusage, setsession, reset,
                                             host=host, port=port, db=db,
                                             user=user, passwd=passwd,
                                             charset=charset,
                                             cursorclass=pymysql.cursors.DictCursor,
                                             ping=1
                                             )
        self._conn = None
        self._cursor = None
        self.__get_conn()

    def __get_conn(self):
        self._conn = self.__pool.connection()
        self._cursor = self._conn.cursor()

    def close(self):
        try:
            self._cursor.close()
            self._conn.close()
        except Exception as e:
            print(e)

    def __execute(self, sql, param=()):
        count = self._cursor.execute(sql, param)
        # print(count)
        return count

    @staticmethod
    def __dict_datetime_obj_to_str(result_dict):
        if result_dict:
            result_replace = {k: int(time.mktime(v.timetuple())) for k, v in result_dict.items(
            ) if isinstance(v, datetime.datetime)}
            result_dict.update(result_replace)
        return result_dict

    def select_one(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._cursor.fetchone()
        result = self.__dict_datetime_obj_to_str(result)
        return count, result

    def select_many(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._cursor.fetchall()
        [self.__dict_datetime_obj_to_str(row_dict) for row_dict in result]
        return count, result

    def execute(self, sql, param=()):
        count = self.__execute(sql, param)
        return count

    def insert_one(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._conn.commit()
        return count, result

    def delete_one(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._conn.commit()
        return count, result

    def update_one(self, sql, param=()):
        count = self.__execute(sql, param)
        result = self._conn.commit()
        return count, result

    def begin(self):
        """开启事务"""
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """结束事务"""
        if option == 'commit':
            self._conn.autocommit()
        else:
            self._conn.rollback()


def Times():
    return int(time.time())


def checkToken(token):
    if token is None:
        return False, {"code": 103, "msg": "孩子你还没登陆呢，在想什么呢？"}
    try:
        jwt_decode = jwt.decode(
            token, '123456', issuer='Issuer', algorithms=['HS256'])['data']
        return True, jwt_decode
    except:
        return False, {"code": 102, "msg": "Token认证失败"}


def getToken(id, user, name, permission):
    d = {
        'exp': time.time() + 2592000,  # 30天
        'iat': time.time(),  # (Issued At) 指明此创建时间的时间戳
        'iss': 'Issuer',  # (Issuer) 指明此token的签发者
        'data': {
            'id': id,
            'user': user,
            'name': name,
            'permission': permission,
            'timestamp': time.time()
        }
    }
    jwt_encode = jwt.encode(d, '123456', algorithm='HS256')
    return jwt_encode


@app.route('/login/', methods=["POST"])
def login():
    mc = MysqlClient()
    user = request.json.get("user")
    pswd = request.json.get("pswd")
    isToken = request.json.get("type") == "token"
    if isToken:
        check, jwt_decode = checkToken(request.cookies.get("token"))
        if not check:
            return jwt_decode
        cc, data = mc.select_one("SELECT * FROM `user` WHERE `id`=%s", (jwt_decode["id"]))
    else:
        cc, data = mc.select_one("SELECT * FROM `user` WHERE `user`=%s", (user))
    if cc == 0:
        return {"code": 101, "msg": "没有该账号!!"}

    if isToken:
        del data['password']
        return {"code": 200, "data": data}
    elif check_password_hash(data['password'], pswd):
        del data['password']
        token = getToken(data['id'], data['user'],
                         data['name'], data['permission'])
        return {"code": 200, "data": data, "token": token}
    else:
        return {"code": 100, "msg": "用户名或者密码错误!!"}


@app.route('/getPostList/', methods=["POST"])
def getPostList():
    mc = MysqlClient()
    data = request.json
    check, jwt_decode = checkToken(request.cookies.get("token"))
    sql = """
    SELECT post.userid, post.id, title, type, content
	, update_time, post_time, `link`, imgs, gender
	, `name`, avatar, zan, scang,topic_id
    FROM post, user
    WHERE post.userid = user.id 额外参数
    ORDER BY post_time DESC
    LIMIT %s, 10
    """
    if data.get("type") == "topic":
        total = mc.select_one(f"SELECT COUNT(*) AS total FROM post WHERE JSON_CONTAINS(topic_id,JSON_Array({data.get('topic_id')}))")[1]
        sql = sql.replace("额外参数", f"AND JSON_CONTAINS(topic_id,JSON_Array({data.get('topic_id')}))")
    else:
        sql = sql.replace("额外参数", "")
        total = mc.select_one("SELECT COUNT(*) AS total FROM post")[1]
    postdata = mc.select_many(sql, ((data.get("limit") - 1) * 10))[1]

    plun = mc.select_many(
        "SELECT COUNT(*) AS plun_num, postid FROM `comment` GROUP BY postid")[1]
    plun_num = {}
    for i in plun:
        plun_num[i["postid"]] = i["plun_num"]

    for i in range(0, len(postdata)):
        if len(postdata[i]['content']) > 400:
            postdata[i]['content'] = postdata[i]['content'][:399] + '···'
        postdata[i]['imgs'] = json.loads(postdata[i]['imgs'])
        postdata[i]['topic_id'] = json.loads(postdata[i]['topic_id'])
        zan = json.loads(postdata[i]['zan'])
        scang = json.loads(postdata[i]['scang'])

        postdata[i]['zan_num'] = len(zan)
        postdata[i]['scang_num'] = len(scang)
        if check:
            postdata[i]['zan'] = str(jwt_decode["id"]) in zan
            postdata[i]['scang'] = str(jwt_decode["id"]) in scang
        else:
            postdata[i]['zan'] = False
            postdata[i]['scang'] = False
        postdata[i]['plun_num'] = plun_num.get(postdata[i]['id'], 0)

    return {"code": 200, "data": json.loads(json.dumps(postdata)), "total": total['total']}


@app.route('/getCommentList/', methods=["POST"])
def getComment():
    mc = MysqlClient()
    data = request.json
    sql = """
        SELECT `comment`.id, postid, userid, content, imgs
        , comment_time, update_time, permission, gender, name
        , avatar,`comment`.comment,zan
        FROM `comment`, `user`
        WHERE `user`.id = `comment`.userid
            AND postid = %s
        ORDER BY comment_time, `comment`.id
        LIMIT %s, 10
    """
    postdata = mc.select_many(
        sql, (data.get("postid"), (data.get("limit") - 1) * 10))[1]

    for i in range(0, len(postdata)):
        postdata[i]['imgs'] = json.loads(postdata[i]['imgs'])
        postdata[i]['zan'] = json.loads(postdata[i]['zan'])
        postdata[i]['comment'] = json.loads(postdata[i]['comment'])
    return {"code": 200, "data": postdata}


@app.route('/register/', methods=["POST"])
def register():
    mc = MysqlClient()
    user = request.json.get("user")
    password = generate_password_hash(request.json.get("pswd"))
    name = user
    sql = "insert into user(user,password,name) values (%s,%s,%s)"
    mc.insert_one(sql, (user, password, name))
    return {"code": 200, "msg": "注册成功"}


@app.route('/judge/', methods=["GET", "POST"])
def judge():
    mc = MysqlClient()
    _type = request.args.get('type')
    data = request.args.get('data')
    if _type == "user":
        if mc.select_one("select * from user where user=%s", data)[0] > 0:
            return {"code": 301, "msg": "已经有该账号了！！", "state": False}
        else:
            return {"code": 200, "msg": "没有这个账号", "state": True}


@app.route('/operate/', methods=["POST"])
def operate():
    mc = MysqlClient()
    data = request.json
    _type = data.get("type")
    check, jwt_decode = checkToken(request.cookies.get("token"))
    if not check:
        return jwt_decode

    if data.get("type") == "zan" or data.get("type") == "scang":
        if data.get("post_userid") == jwt_decode["id"]:
            return {"code": 500, "msg": "不能对自己帖子进行操作哦！"}

        if not data.get("isCancel"):  # 添加
            # Key为用户id,value为时间戳
            sql = f"UPDATE post set {_type}=JSON_INSERT({_type}, '$.\"%s\"','%s' ) WHERE id=%s"
            if mc.insert_one(sql, (jwt_decode["id"], Times(), data.get("postid")))[0]:
                return {"code": 200, "msg": f"{_type}帖子点赞成功", "ty": "add"}
            else:
                return {"code": 201, "msg": f"{_type}数据库错误", "ty": "add"}

        elif data.get("isCancel"):  # 取消
            # Key为用户id,value为时间戳
            sql = f"UPDATE post set {_type}=json_remove({_type}, '$.\"%s\"') WHERE id=%s"
            if mc.insert_one(sql, (jwt_decode["id"], data.get("postid")))[0]:
                return {"code": 200, "msg": f"{_type}取消成功", "ty": "re"}
            else:
                return {"code": 201, "msg": f"{_type}数据库错误", "ty": "re"}

    elif data.get("type") == "comment_zan":
        if data.get("comment_userid") == jwt_decode["id"]:
            return {"code": 500, "msg": "不能对自己帖子进行操作哦！"}

        if not data.get("isCancel"):  # 添加
            # sql = """
            # UPDATE `forum`.`comment` SET
            #     `zan` = json_array_append(`zan`,'$', CAST('{"uid": %s,"date": %s}' AS JSON))
            #     WHERE `id` = %s;
            # """
            sql = """
            UPDATE `forum`.`comment` SET 
            `zan` = JSON_INSERT(`zan`,'$.\"%s\"','%s') WHERE `id` = %s;
            """
            if mc.insert_one(sql, (jwt_decode["id"], Times(), data.get("commentid")))[0]:
                return {"code": 200, "msg": f"{_type}评论点赞成功", "ty": "add"}
            else:
                return {"code": 201, "msg": f"{_type}数据库错误", "ty": "add"}

        elif data.get("isCancel"):  # 取消
            sql = """
            UPDATE `forum`.`comment` SET 
                `zan` = json_array_append(`zan`,'$', CAST('{"uid": %s,"date": %s}' AS JSON))
                WHERE `id` = %s;
            """
            if mc.insert_one(sql, (jwt_decode["id"], Times(), data.get("commentid")))[0]:
                return {"code": 200, "msg": f"{_type}评论点赞成功", "ty": "re"}
            else:
                return {"code": 201, "msg": f"{_type}数据库错误", "ty": "re"}


@app.route('/upload/', methods=["POST"])
def upload():
    data = request.form
    check, jwt_decode = checkToken(request.cookies.get("token"))
    if not check:
        return jwt_decode
    if data["type"] in ["avatar", "RichText", "ImageText", "PureGraph"]:
        file_obj = request.files.get("file")
        filename = secure_filename(file_obj.filename)
        if file_obj is None:
            return "文件上传为空"
        # 文件名id-时间戳-后缀名
        filename = f"{jwt_decode['id']}-{time.time()}.{filename.split('.')[-1]}"
        file_obj.save(os.path.join(f'files/{data["type"]}', filename))
        #         return {"code": 200, "msg": "成功", "url": f"/files/{data['type']}/{filename}"}
        return {
            "errno": 0,
            "data": {
                "url": f"/files/{data['type']}/{filename}",
                "href": f"/files/{data['type']}/{filename}",
            }
        }
    else:
        return {
            "errno": 1,
            "message": "图片上传失败............."
        }


@app.route('/sendPost/', methods=["POST"])
def sendPost():
    mc = MysqlClient()
    data = request.json
    check, jwt_decode = checkToken(request.cookies.get("token"))
    if not check:
        return jwt_decode
    if data.get("type") == "PureGraph":
        sql = """
        INSERT INTO `forum`.`post` (`userid`, `title`, `type`, `content`, `link`
            , `imgs`, `zan`, `scang`,`topic_id`)
        VALUES (%s, %s, %s, %s, %s
            , %s, '{}', '{}','{}');
        """
        if mc.insert_one(sql, (jwt_decode["id"], data['title'], data['type'], data['content'], data['link'], str(data['imgs']).replace("'", "\"")))[0]:
            return {"code": 200, "msg": "发布成功！"}
        else:
            return {"code": 201, "msg": f"数据库错误", "ty": "re"}


@app.route('/sendComment/', methods=["POST"])
def sendComment():
    mc = MysqlClient()
    data = request.json
    check, jwt_decode = checkToken(request.cookies.get("token"))
    if not check:
        return jwt_decode
    sql = """
    INSERT INTO `forum`.`comment` (`postid`, `userid`, `content`, `imgs`,`comment`,`zan`) VALUES (%s, %s, %s, %s,'[]','[]');
    """
    mc.insert_one(sql, (data["postid"], jwt_decode["id"],
                        data["content"], str(data['imgs']).replace("'", "\"")))
    return {"code": 200, "msg": "评论成功！"}


@app.route('/getPost/', methods=["POST"])
def getPost():
    mc = MysqlClient()
    data = request.json
    sql = """
    SELECT post.userid, post.id, title, type, content
	, update_time, post_time, `link`, imgs, gender
	, `name`, avatar, zan, scang
    FROM post, user
    WHERE post.userid = user.id
    AND post.id = %s
    """
    post_num, postdata = mc.select_one(sql, data.get("postid"))
    if post_num != 0:
        plun = mc.select_one(
            "SELECT COUNT(*) AS plun_num, postid FROM `comment` WHERE postid=%s", (data.get("postid")))[1]

        postdata['imgs'] = json.loads(postdata['imgs'])
        postdata['zan'] = json.loads(postdata['zan'])
        postdata['scang'] = json.loads(postdata['scang'])
        postdata['plun_num'] = plun["plun_num"]
        return {"code": 200, "data": json.loads(json.dumps(postdata))}
    else:
        return {"code": 404, "msg": "没有获取到帖子信息"}


@app.route('/getMyFile/')
def getMyFile():
    mc = MysqlClient()
    check, jwt_decode = checkToken(request.cookies.get("token"))
    if not check:
        return jwt_decode
    post_num, Myfile = mc.select_one('SELECT * FROM `uconfig` WHERE uid=%s AND type="myFile"', jwt_decode["id"])
    if post_num:
        MyFileList = json.loads(Myfile["data"])
        return {"code": 200, "data": MyFileList}
    else:
        return {"code": 404, "msg": f"没有获取到文件夹配置"}


@app.route('/getTopic/', methods=["POST"])
def getTopic():
    mc = MysqlClient()
    cc, topicData = mc.select_many("SELECT * FROM topic")

    if cc == 0:
        return {"code": 101, "msg": "没有数据"}
    else:
        topics = {}
        for topic in topicData:
            topics[topic["id"]] = topic
        return {"code": 200, "data": topics}


@app.route('/getmyPost/', methods=["POST"])
def getmyPost():
    mc = MysqlClient()
    data = request.json
    check, jwt_decode = checkToken(request.cookies.get("token"))
    if not check:
        return jwt_decode
    Sql = f'SELECT * FROM `post`,user WHERE JSON_CONTAINS_PATH({data["type"]}, \'one\', \'$."%s"\') AND post.userid = user.id ORDER BY post_time DESC'
    if data["type"] == "my":
        cc, PostDATA = mc.select_many(
            "SELECT * FROM `post`,user WHERE userid=%s AND post.userid = user.id ORDER BY post_time DESC ", jwt_decode["id"])
    elif data["type"] in ["zan", "scang"]:
        cc, PostDATA = mc.select_many(Sql, jwt_decode["id"])
    else:
        return {"code": 102, "msg": "类型错误"}
    if cc == 0:
        return {"code": 101, "msg": "没有数据"}
    else:

        plun = mc.select_many(
            "SELECT COUNT(*) AS plun_num, postid FROM `comment` GROUP BY postid")[1]
        plun_num = {}
        for i in plun:
            plun_num[i["postid"]] = i["plun_num"]
        for i in range(0, len(PostDATA)):
            del PostDATA[i]['password']
            if len(PostDATA[i]['content']) > 400:
                PostDATA[i]['content'] = PostDATA[i]['content'][:399] + '···'
            PostDATA[i]['imgs'] = json.loads(PostDATA[i]['imgs'])
            PostDATA[i]['topic_id'] = json.loads(PostDATA[i]['topic_id'])
            zan = json.loads(PostDATA[i]['zan'])
            scang = json.loads(PostDATA[i]['scang'])

            PostDATA[i]['zan_num'] = len(zan)
            PostDATA[i]['scang_num'] = len(scang)
            if check:
                PostDATA[i]['zan'] = str(jwt_decode["id"]) in zan
                PostDATA[i]['scang'] = str(jwt_decode["id"]) in scang
            else:
                PostDATA[i]['zan'] = False
                PostDATA[i]['scang'] = False
            PostDATA[i]['plun_num'] = plun_num.get(PostDATA[i]['id'], 0)
        return {"code": 200, "data": PostDATA}


if __name__ == "__main__":
    """
    100用户名密码错误
    101没有该账号
    102Token认证失败
    103没有登陆
    201数据库错误
    200成功
    301已经有账号了
    302上传类型不符
    404没获取到帖子
    500不能对自己帖子评价
    """
    app.run(debug=True)
