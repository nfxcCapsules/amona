#coding:utf-8

import requests
import base64
import os

# #前置条件：登录console
#
# loginUrl = "http://test.sobot.com/basic/serviceLogin/4"
#
# loginUser = "wangkun@gmail.com"
# loginPwd = "sobot123"
# loginFlag = 1
# loginPwd_base64 = base64.b64encode(loginPwd.encode("utf-8"))
# loginPwd_str = str(loginPwd_base64,"utf-8")
# print(str(loginPwd_base64,"utf-8"))
# print(loginPwd_str)
#
# payload = {
#     "loginUser":loginUser,
#     "loginPwd":loginPwd_str,
#     "loginFlag":loginFlag
# }
#
# r = requests.post(url=loginUrl,data=payload)
# result = r.json()
#
#
# if r.status_code == 200 and result["retCode"] == "000000":
#     print("测试结果：登录成功")
# else:
#     print("测试失败:%s"%(result["retMsg"]))



#文件上传接口
fileUploadUrl = "http://test.sobot.com/chat/webchat/fileupload.action"

#遍历文件夹
rootdir = "D:\\Dev\\workspace\\sobotConsole\\files\\"
l = os.listdir(rootdir) #列出文件夹下所有的目录与文件
print("输出所有文件：",l)
print(type(l))
# for i in range(0,len(l)):
#     path = os.path.join(rootdir,l[i])
#     print("输出所有文件路径：",path)
# #     if os.path.isfile(path): #你想对文件的操作

# files = {
#     "file":open("D:\\Dev\\workspace\\sobotConsole\\files\\001.mp4","rb")
# }

for i in range(0,len(l)):
    files = {
    "file":open("D:\\Dev\\workspace\\sobotConsole\\files\\"+l[i],"rb")
    }
    payload = {
      # "file":files["file"],
      "type":"msg",
      "pid":"99cab16ac91e456c9d67272e09f964c8",
      "countTag":"1",
      "source":"0"
    }

    upload_res = requests.post(url=fileUploadUrl,files=files,data=payload)
    result = upload_res.json()

    if upload_res.status_code == 200 and result["countTag"] == "1":
        print("测试用例执行成功,执行结果显示：%s"%result)

    else:
        print("测试用例执行失败，失败原因：%s"%result)

# print(result)
# print(upload_res.status_code)