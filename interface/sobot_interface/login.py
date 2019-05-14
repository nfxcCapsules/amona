# coding:utf-8

import requests
import base64
import time
import datetime

loginUrl = "http://test.sobot.com/basic/serviceLogin/4"

loginUser = "wangkun@gmail.com"
loginPwd = "sobot123"
loginFlag = 1
loginPwd_base64 = base64.b64encode(loginPwd.encode("utf-8"))
loginPwd_str = str(loginPwd_base64,"utf-8")
print(str(loginPwd_base64,"utf-8"))
print(loginPwd_str)

payload = {
    "loginUser":loginUser,
    "loginPwd":loginPwd_str,
    "loginFlag":loginFlag
}

r = requests.post(url=loginUrl,data=payload)
result = r.json()


if r.status_code == 200 and result["retCode"] == "000000":
    print("测试结果：登录成功")
else:
    print("测试失败:%s"%(result["retMsg"]))


#运行质检任务
time_str = time.strftime("%Y-%m-%d",time.localtime())
print("time_str",time_str)
print()
sessionStartTime = time_str + " 00:00:00"
print("sessionStartTime",sessionStartTime)
sessionEndTime = time_str + " 23:59:59"
print("sessionEndTime",sessionEndTime)



taskUrl = "http://test.sobot.com/cloudapi/sobot-inspection-job/job/verify/now"

headers = {
    "Content-Type":"application/json",
    "temp-id":result["item"]
}

payload = {
    "sessionEndTime":"2019-04-16 23:59:59",
    "sessionStartTime":"2019-04-16 00:00:00",
    "taskId":"9b6f90ef71a642b8b636c335ed819491"
}

rep_task = requests.post(url=taskUrl,headers=headers,json=payload)
print(rep_task.text)