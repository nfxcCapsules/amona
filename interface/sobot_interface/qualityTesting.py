# coding:utf-8

import requests
import base64

loginUrl = "https://www.sobot.com/basic/serviceLogin/4"

loginUser = "amona@sobot.com"
loginPwd = "sobot123"
loginPwd_base64 = base64.b64encode(loginPwd.encode("utf-8"))
loginPwd_str = str(loginPwd_base64,"utf-8")
print(loginPwd_base64)
print(loginPwd_str)

loginPayload = {
    "loginUser":loginUser,
    "loginPwd":loginPwd_str,
    "loginFlag":1
}

r_login = requests.post(url=loginUrl,json=loginUrl)
result_login = r_login.json()
print(result_login)