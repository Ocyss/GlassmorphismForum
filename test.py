import requests


url = "http://127.0.0.1:5000/"

req = requests.post(url+"getPost", json={"postid": 1})

print(req)
print(req.text)
