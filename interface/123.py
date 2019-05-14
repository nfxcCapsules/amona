# coding:utf-8
import requests
import time
# import datetime
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()


# today = datetime.date.today()
# print("today_date",today_date)
# today_str = today_date.strftime("%Y-%m-%d")
# print("today_str",today_str)
# yestoday_date = today_date - datetime.timedelta(days=1)
# print("yestoday_date",yestoday_date)
# yestoday_str = yestoday_date.strftime("%Y-%m-%d")
# print("yestoday_str",yestoday_str)
# today_stamp = time.mktime(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
# print(time.strptime(today_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
# print("today_stamp",today_stamp)
# yestoday_stamp = time.mktime(time.strptime(yestoday_str + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
# print("yestoday_stamp",yestoday_stamp)


# tomorrow = today + datetime.timedelta(days=1)
# print(tomorrow)
# acquire = today + datetime.timedelta(days=2)
# print(acquire)
fileUploadUrl = "http://test.sobot.com/chat/webchat/fileupload.action"
files = {
"file": open("D:\\Dev\\workspace\\sobotConsole\\files\\006.xmind", "rb")
}
payload = {
# "file":files["file"],
"type": "msg",
"pid": "99cab16ac91e456c9d67272e09f964c8",
"countTag": "1",
"source": "0"
}

upload_res = requests.post(url=fileUploadUrl, files=files, data=payload)
result = upload_res.json()
print(result)