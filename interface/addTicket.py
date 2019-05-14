# coding:utf8

import requests
import base64


host = "https://test.sobot.com"
loginUrl = "/console/login"
pwd = "sobot123"
password = base64.b64encode(pwd.encode('utf-8')).decode("utf-8")
print(password)

data = {
 "loginUser":"wangkun@gmail.com",
 "loginPwd" :"sobot123"
}

r = requests.post(host+loginUrl,data=data)
result = r.status_code
print(result)