from email import header
import requests


url = "http://127.0.0.1:5000/"

headers = {
    "Cookie": "userid=1; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjI4OTk1NTQuNTU0MzU0MiwiaWF0IjoxNjYwMzA3NTU0LjU1NDM1NDIsImlzcyI6Iklzc3VlciIsImRhdGEiOnsiaWQiOjEsInVzZXIiOiJhZG1pbiIsIm5hbWUiOiJBZG1pbiIsInBlcm1pc3Npb24iOiJyb290IiwidGltZXN0YW1wIjoxNjYwMzA3NTU0LjU1NDM1NDJ9fQ.aryWFeRKjrrx0-OhDwhktaW2S6S71J3544y954e5Qa0"}

req = requests.post(url+"getPostList", json={"limit": 1}, headers=headers)


print(req)
for i in req.json()["data"]:
    print(i)
    print()
