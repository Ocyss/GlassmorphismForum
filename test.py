import requests
import json

url = "http://127.0.0.1:5000/"

req = requests.post(url+"getPostList",data=json.dumps({"limit":"1"}))

print(req)
print(req.text)