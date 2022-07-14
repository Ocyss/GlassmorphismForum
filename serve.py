import json
import datetime
import pymysql
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

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

@app.route('/login/',methods=["POST"],strict_slashes=False)
def login():
    user = request.form.get("user")
    pswd = request.form.get("pswd")
    print(user,pswd,request.form)
    if cursor.execute("SELECT * FROM `user` WHERE `user`=%s",(user)):
        data = cursor.fetchall()[0]
        if check_password_hash(data['password'],pswd):
            del data['password']
            return {"code":200,"data":data}
        else:
            return {"code":100,"msg":"用户名或者密码错误!!"}

@app.route('/getPostList/',strict_slashes=False)
def getPost():
    if cursor.execute("SELECT post.id,title,type,content,update_time,post_time,'like',imgs,gender,name,avatar FROM post,user WHERE post.userid=user.id"):
        postdata = cursor.fetchall()
        return {"code":200,"data":postdata}
    else:
        return {"code":500,"msg":"没有获取到帖子数据"}


@app.route('/register/',methods=["POST"],strict_slashes=False)
def register():
    user = request.form.get("user")
    password = generate_password_hash(request.form.get("pswd"))
    name=user
    sql = "insert into user(user,password,name) values (%s,%s,%s)"
    if cursor.execute(sql, (user, password, name)):
        conn.commit()
        return {"code":200,"msg":"注册成功"}
    else:
        return {"code":500,"msg":"没有获取到数据"}



if __name__ == "__main__":
    
    app.run(debug=True)