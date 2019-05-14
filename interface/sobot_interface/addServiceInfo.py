# coding:utf-8

import  requests
import time
import random
import hashlib

#电商平台添加企业

#第三方平台唯一编码，智齿提供
#unionCode="10001"

#线上账号join@aliyun.com(unionCode:10002)
unionCode = "10002"

#生成随机系统时间戳
ts=str(round(time.time()))
#print(ts)

#公司名称
companyName = "companyName"+str(random.randint(0,99))

#生成随机邮箱
# email=str(random.randint(0,99999999))+"@qq.com"
#线上阿里云邮箱（商户）
email=str(random.randint(0,99999999))+"@aliyun.com"

#生成随机客服邮箱
# serviceEmail = str(random.randint(0,99999999))+"@qq.com.cn"
#线上阿里云邮箱（客服）
serviceEmail = str(random.randint(0,99999999))+"@aliyun.com.cn"

#指定最大客服数量
maxCount = random.randint(2,5)
print(maxCount)

#客服登录密码
password = "sobot123"

#拼接token
#token = MD5(unionCode+ts+email+unionKey) unionKey：加密私钥由智齿提供 ciqL4ZL2QJqBzJGG
# unionKey="ciqL4ZL2QJqBzJGG"
#线上阿里云unionKey
unionKey="ciqL4ZL2QJqBzJGG"

token_str=unionCode+ts+email+unionKey
b=token_str.encode(encoding="utf-8")
m = hashlib.md5()
m.update(b)
token = m.hexdigest()
print("打印企业token：",token)

token_ser=unionCode+ts+serviceEmail+unionKey
b_ser=token_ser.encode(encoding="utf-8")
m_ser = hashlib.md5()
m_ser.update(b_ser)
serviceToken = m_ser.hexdigest()
print("打印客服token：",serviceToken)

#商户在平台里面的唯一id
customerCode = str(random.randint(1,9999))

#客服真实姓名
name="Test"+str(random.randint(0,99))

#客服昵称
nick=name.lower()


#客户角色ID（5555:工单客服、2222:在线管理员、1111:在线客服、8888:工单管理员）
list_roleId = ["1111","2222","5555","8888"]

roleId = random.choice(list_roleId)
print("输入客户角色Id：",roleId)

#添加企业url
# addTenantUrl = "http://test.sobot.com/tenantpro/open/addTenant.json"
addTenantUrl = "http://www.sobot.com/tenantpro/open/addTenant.json"

#添加企业payload
payload_addTenant = {
    "unionCode":unionCode,
    "ts":ts,
    "companyName":companyName,
    "email":email,
    "maxCount":maxCount,
    "password":password,
    "token":token,
    "customerCode":customerCode
}
print("输出添加企业请求参数：",payload_addTenant)

r_addTenant = requests.post(url=addTenantUrl,data=payload_addTenant)
result_addTenant = r_addTenant.json()
print(result_addTenant)

print("输出添加企业接口测试结果:",r_addTenant.text)
print(result_addTenant["msg"]["sysNum"])
if r_addTenant.status_code == 200 and result_addTenant["retCode"] == "200000" and result_addTenant["msg"]["sysNum"] is not None:
  print("测试用例执行成功！")
else:
  print("测试用例执行失败:%s"%(result_addTenant["retMsg"]))



# #构造测试数据
# pwds = ['','123456','12345678','abcdefgh','1q2w3e4r','!1qa@2ws','12345!@#$%qwertasdfg']
#
# for password in pwds:
#     password
#     print(password)
#
# #password
#
# #addSICUrl ="http://test.sobot.com/tenantpro/open/addServiceInfoConfim.json"
# addSICUrl="http://www.sobot.com/tenantpro/open/addServiceInfoConfim.json"
#
# payload_addSIC = {
#     "unionCode":unionCode,
#     "ts":ts,
#     "token":serviceToken,
#     "customerCode":customerCode,
#     "name":name,
#     "nick":nick,
#     "email":serviceEmail,
#     "roleId":roleId,
#     "password":password
#
# }
# print("输出添加客服请求参数：",payload_addSIC)
#
# r_addSIC = requests.post(url=addSICUrl,data=payload_addSIC)
# result_addSIC = r_addSIC.json()
#
# print("输出添加客服接口测试结果:",r_addSIC.text)
# if r_addSIC.status_code == 200 and result_addSIC["retCode"] == "200000":
#     print("测试用例执行成功!")
# else:
#     print("测试用例执行失败:%s"%(result_addSIC["retMsg"]))
#
#
#
# #登录接口
# #loginUrl = "http://test.sobot.com/basic-login/login/4"
# loginUrl = "https://www.sobot.com/basic-login/login/4"
#
# payload_login = {
#     "loginUser":serviceEmail,
#     "loginPwd":password
#
# }
# print("输出登录用户信息：",payload_login)
#
# r_login =  requests.post(url=loginUrl,json=payload_login)
# result_login = r_login.json()
# print(r_login.text)
# if r_login.status_code == 200 and result_login["retCode"] == "000000":
#     print("测试结果：登录成功")
# else:
#     print("测试失败:%s"%(result_login["retMsg"]))
#
#
# #服务总结接口
# serviceUrl = ""
