import json
import datetime
from re import T
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
    if cursor.execute("SELECT post.id,title,type,content,update_time,post_time,'like',imgs,gender,name,avatar FROM post,user WHERE post.userid=user.id"):
        postdata = cursor.fetchall()
        return {"code":200,"data":postdata}
    else:
        return {"code":500,"msg":"没有获取到帖子数据"}

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


@app.route('/operate/',methods=["GET","POST"])
def operate():
    data = request.json




if __name__ == "__main__":
    app.run(debug=True)