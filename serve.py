import json
import datetime
from re import L, T
from matplotlib.pyplot import get
import pymysql
import jwt
import time
from flask import Flask,request,make_response,jsonify
from werkzeug.security import generate_password_hash,check_password_hash


conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='forum',
    charset='utf8mb4'
)
cursor = conn.cursor(pymysql.cursors.DictCursor)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['OPENAPI_VERSION'] = '3.0.2'
app.url_map.strict_slashes = False
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)


def getToken(id,user,name,permission):
    d = {
        'exp':time.time()+2592000, # 30天
        'iat':time.time(), # (Issued At) 指明此创建时间的时间戳
        'iss':'Issuer', # (Issuer) 指明此token的签发者
        'data':{
            'id':id,
            'user':user,
            'name':name,
            'permission':permission,
            'timestamp':time.time()
        }
    }
    jwt_encode = jwt.encode(d,'123456',algorithm='HS256')
    return jwt_encode

@app.route('/login/',methods=["POST"])
def login():
    user = request.json.get("user")
    pswd = request.json.get("pswd")
    if cursor.execute("SELECT * FROM `user` WHERE `user`=%s",(user)):
        data = cursor.fetchall()[0]
        if check_password_hash(data['password'],pswd):
            del data['password']
            token = getToken(data['id'],data['user'],data['name'],data['permission'])
            return {"code":200,"data":data,"token":token}
        else:
            return {"code":100,"msg":"用户名或者密码错误!!"}

@app.route('/getPostList/')
def getPost():
    if cursor.execute("SELECT post.userid,post.id,title,type,content,update_time,post_time,'like',imgs,gender,name,avatar,zan,scang,zan_num,scang_num FROM post,user WHERE post.userid=user.id"):
        postdata = cursor.fetchall()
        for i in range(0,len(postdata)):
            if len(postdata[i]['content']) > 400:
                postdata[i]['content'] = postdata[i]['content'][:399]+'···'
            postdata[i]['post_time'] = int(time.mktime(postdata[i]['post_time'].timetuple()))
            postdata[i]['update_time'] = int(time.mktime(postdata[i]['update_time'].timetuple()))
            postdata[i]['zan'] = json.loads(postdata[i]['zan'])
            postdata[i]['scang'] = json.loads(postdata[i]['scang'])
        return {"code":200,"data":json.loads(json.dumps(postdata,cls=DateEncoder))}
    else:
        return {"code":500,"msg":"没有获取到帖子数据"}

@app.route('/getCommentList/',methods=["POST"])
def getComment():
    data = request.json
    sql = "SELECT `comment`.id,postid,userid,content,imgs,comment_time,update_time,permission,gender,name,avatar FROM `comment`,`user` WHERE `user`.id=`comment`.userid AND postid=%s ORDER BY comment_time,`comment`.id"
    if cursor.execute(sql,(data.get("postid"))):
        postdata = cursor.fetchall()
        for i in range(0,len(postdata)):
            if len(postdata[i]['content']) > 400:
                postdata[i]['content'] = postdata[i]['content'][:399]+'···'
            postdata[i]['comment_time'] = int(time.mktime(postdata[i]['comment_time'].timetuple()))
            postdata[i]['update_time'] = int(time.mktime(postdata[i]['update_time'].timetuple()))
        return {"code":200,"data":json.loads(json.dumps(postdata,cls=DateEncoder))}
    else:
        return {"code":500,"msg":"没有获取到评论数据"}

@app.route('/register/',methods=["POST"])
def register():
    user = request.json.get("user")
    password = generate_password_hash(request.json.get("pswd"))
    name=user
    sql = "insert into user(user,password,name) values (%s,%s,%s)"
    if cursor.execute(sql, (user, password, name)):
        conn.commit()
        return {"code":200,"msg":"注册成功"}
    else:
        return {"code":500,"msg":"没有获取到数据"}


@app.route('/judge/',methods=["GET","POST"])
def judge():
    _type = request.args.get('type')
    data = request.args.get('data')
    print(_type,data)
    if _type == "user":
        if cursor.execute("select * from user where user=%s",data):
            cursor.fetchall()
            return {"code":301,"msg":"已经有该账号了！！","state":False}
        else:
            return {"code":200,"msg":"没有该账号","state":True}


@app.route('/operate/',methods=["POST"])
def operate():
    data = request.json
    token = request.cookies.get("token")
    try:
        jwt_decode = jwt.decode(token, '123456', issuer='Issuer',  algorithms=['HS256'])['data']
    except:
        return {"code":101,"msg":"Token认证失败"}

    if data.get("type") == "zan" or data.get("type") == "scang":
        if data.get("post_userid") == jwt_decode["id"]:
            return {"code":500,"msg":"不能对自己帖子进行操作哦！"}
        
        if not data.get("isCancel"): #添加
            sql = f"UPDATE post set {data.get('type')}=JSON_INSERT({data.get('type')}, '$.\"%s\"','%s' ),{data.get('type')}_num={data.get('type')}_num+1 WHERE id=%s" # Key为用户id,value为时间戳

            if cursor.execute(sql,(jwt_decode["id"],int(time.time()),data.get("postid"))):
                conn.commit()
                return {"code":200,"msg":f"{data.get('type')}添加成功","ty":"add"}
            else:
                {"code":301,"msg":f"{data.get('type')} 数据库未知操作错误！"}
        
        elif data.get("isCancel"): #取消
            sql = f"UPDATE post set {data.get('type')}=json_remove({data.get('type')}, '$.\"%s\"'),{data.get('type')}_num={data.get('type')}_num-1 WHERE id=%s" # Key为用户id,value为时间戳
            if cursor.execute(sql,(jwt_decode["id"],data.get("postid"))):
                conn.commit()
                return {"code":200,"msg":f"{data.get('type')}取消成功","ty":"re"}
            else:
                {"code":301,"msg":f"{data.get('type')} 数据库未知操作错误！"}


    elif data.get("type") == "plun":
        pass




if __name__ == "__main__":
    app.run(debug=True)