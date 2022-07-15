import requests

url = "http://127.0.0.1:5000/"

req = requests.post(url+"operate",data={"post_userid":2,"postid":"admin"})

print(req)
print(req.text)