import requests

url = "http://127.0.0.1:5000/"

req = requests.post(url+"login",data={"user":"admin","pswd":"admin"})

print(req)
print(req.text)