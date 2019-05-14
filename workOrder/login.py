# coding:utf-8

from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
driver.get("https://test.sobot.com/console/login")
time.sleep(5)

#浏览器窗口最大化
#driver.maximize_window()
#time.sleep(3)

#登录验证
uesrEmail = driver.find_element_by_id("userEmail").send_keys("wangkun@gmail.com")
userPassword = driver.find_element_by_id("userPassword").send_keys("sobot123")
reg_submit = driver.find_element_by_class_name("reg_submit").click()
time.sleep(5)

userName = driver.find_element_by_class_name("loginSetting_name").text
print("获取登录用户账号信息：%s" %userName)

if userName =="昆儿":
    print("登录成功！！！")
else:
    print("登录失败！！！")

#工单中心
driver.find_element_by_class_name("sidebarIcon-workOrder").click()
time.sleep(5)

workOrder = driver.find_element_by_link_text("工单中心").text

if workOrder == "工单中心":
    print("进入工单中心成功！！！")
else:
    print("进入工单中心失败！！！")

#添加工单
driver.find_element_by_class_name("btn-add-sm").click()
time.sleep(2)
ticketTitle = driver.find_element_by_class_name("ng-invalid-required").text
print("获取工单标题：%s" %ticketTitle)

if not ticketTitle :
    print("进入新建工单页面成功！！！")
else:
    print("进入新建工单页面失败！！！")

ticketType = driver.find_element_by_class_name("js-classify-init").click()
time.sleep(2)
typeName = driver.find_element_by_link_text("其他").text
print("获取工单分类列表：%s" %typeName)

if typeName == "其他":
    print("进入工单分类列表,操作成功！！！")
else:
    print("进入工单分类列表,操作失败！！！")

#选择工单分类
driver.find_element_by_link_text("其他").click()

#添加工单标题
ticketTitle = "工单自动化测试_" + str(random.randint(0,99999))
driver.find_element_by_class_name("ng-invalid-required").send_keys(ticketTitle)

#添加问题描述（iframe）

#切换iframe环境
driver.switch_to_frame("ueditor_0")
problemDes = driver.find_element_by_tag_name("body").send_keys(ticketTitle)

#释放iframe，重新回到主页面上
driver.switch_to_default_content()

#js操作滚动条
js = 'document.querySelector(".zc-ws-add-outer-body").scrollTop=10000'
driver.execute_script(js)
time.sleep(3)


#选择相关客户
client = driver.find_element_by_css_selector("[ng-bind='formData.customer.nick']").text
print(client)
if client == "--":
    print("定位相关客户列表成功！！！")
else:
    print("定位相关客户列表失败！！！")

driver.find_element_by_css_selector("[ng-bind='formData.customer.nick']").click()
time.sleep(2)

#输入客户信息并选择
driver.find_element_by_css_selector("[placeholder='搜索客户姓名/昵称/电话/邮箱']").send_keys("test")
time.sleep(2)
driver.find_element_by_css_selector("[ng-bind='item.nick']").click()

#点击提交按钮
driver.find_element_by_css_selector("[ng-click='quickCreate()']").click()

time.sleep(5)
driver.quit()
