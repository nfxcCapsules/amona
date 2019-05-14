# coding:utf-8

import requests
import hashlib
import time
import json
#url = "https://open.sobot.com/open/platform/api.json"

# r = requests.post(url)
# data = r.json()
# print(data)

#智齿分配的appId
appId = "6cfcb1a29f2c4981a7f64d5b1dfcf62f"

#自1970年1月1日0时起至今的毫秒数
createTime =str(round(time.time())*1000)
print(createTime)

#签名（appId,appKey,createTime以字符串方式拼接后经过MD5加密）
appKey="b7FamknBuh6A"

signOld = str(appId+appKey+createTime)
b = signOld.encode(encoding="utf-8")
m = hashlib.md5()
m.update(b)
sign = m.hexdigest()
print(sign)

#token过期时间，单位小时(可传入大于0，小于25的整数)
expire = "24"
#获取token
payload = {
    "appId":appId,
    "createTime":createTime,
    "sign":sign,
    "expire":"24"
}
print(createTime)
url = "https://www.sobot.com/open/platform/getAccessToken.json"

r = requests.get(url,params=payload)
print(r.url)
result = r.json()
print(type(result))
print(result)
access_token = result["data"]["access_token"]
print(result["data"]["access_token"])


serviceUrl = "https://www.sobot.com/open/platform/api.json"
headers = {
    "content-type":"application/json"
}

payload = {"action":"wb_conversation_summary",
           "access_token":access_token,
           "data":{"cid":"ab937c386a404f13b2c49871955862bb"}
           }

#res = requests.post(url=serviceUrl,json=payload)
res = requests.post(url=serviceUrl,data=json.dumps(payload))
print(res.status_code)
print(res.text)

#【需求5397】在线-质检重检导致数据错误

qualityUrl = "https://www.sobot.com/open/platform/api.json"

qualityPayload = {
    "action": "wb_quality_result",
    "access_token": access_token,
    "data": {
      "startDate": "2019-04-01",
      "endDate":"2019-04-18",
      "page":1,
      "size":100
    }
}

r_qua = requests.post(url=qualityUrl,json=qualityPayload)
result_qua = r_qua.json()
print("=======质检结果=======",result_qua)