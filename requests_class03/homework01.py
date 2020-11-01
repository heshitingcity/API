#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/9/26  17:34
# @User : city
# @File : API  homework01.py
# @Author : City


import requests
import re
import jsonpath
import json
from collections import OrderedDict



host = 'http://47.107.178.45'
sesion_info = requests.session()
headers_info = {
	"X-Requested-With": "XMLHttpRequest",
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Accept-Language": "zh-CN,zh;q=0.9"

}



class PHPwind(object):
	def __init__(self,username,password):
		self.username = username
		self.password = password
		# print(self.username)
		# print(self.password)


	#打开系统首页
	def openIndex(self):
		response = sesion_info.get(url='%s/phpwind/'%host)
		body = response.content.decode('utf-8')
		token_id = re.findall('name="csrf_token" value="(.+?)"/>',body)[0]
		print("提取到的token是："+token_id)
		return token_id


	#01、账号登录1
	def Login1(self):
		login_params = {
			"username":self.username,
			"password":self.password,
			"csrf_token":PHPwind.openIndex(self),
			"csrf_token":PHPwind.openIndex(self)
		}
		response1 = sesion_info.post(url='%s/phpwind/index.php?m=u&c=login&a=dologin'%host,
		                          data=login_params,
		                          headers = headers_info)

		print(response1.cookies)

		# body1 = response1.text
		# dologinId = re.json('&_statu=(.+?)","refresh"',body1)[0]

		json_object1 =  str(response1.json())
		dologinId = re.findall("&_statu=(.+?), 'refresh'",json_object1)
		print(dologinId)
		return dologinId

	#01、账号登录2，返回cookies信息
	def Login2(self):
		login_params = {
			"username":self.username,
			"password":self.password,
			"csrf_token":PHPwind.openIndex(self),
			"csrf_token":PHPwind.openIndex(self)
		}
		response1 = sesion_info.post(url='%s/phpwind/index.php?m=u&c=login&a=dologin'%host,
		                          data=login_params,
		                          headers = headers_info)
		cookies_info = response1.cookies.get_dict()
		# sesion_info.update(response1.cookies)
		print(cookies_info)
		return cookies_info




	#02、登录成功
	def login_success(self):
		get_data_params ={
		      "m":"u",
			  "c":"login",
			  "a":"welcome",
			  "_statu":PHPwind.Login1(self)
		}

		response2 = sesion_info.get(url='%s/phpwind/index.php'%host,
		                            params= get_data_params
		                             )
		print(response2.content.decode('utf-8'))
		print('登录成功！')


	#03、发帖
	def send_messege(self):
		messege_params = OrderedDict(
			[
				 ("atc_title",(None,'City of Stars1122')),
				 ("atc_content",(None,'request发帖打卡1222')),
				 ("pid",(None,'')),
				 ("tid",(None,'')),
				 ("special",(None,'default')),
				 ("reply_notice",(None,1)),
				 ("csrf_token",(None,PHPwind.openIndex(self)))
			         ]
		)
		response3 = sesion_info.post(url='%s/phpwind/index.php?c=post&a=doadd&_json=1&fid=57'%host,
		                             files= messege_params
		                             )
		print(response3.json())


    #04、注册
	def register_id(self):
		register_info ={
			"username":"t1109",
			"password":123456,
			"repassword":123456,
			"email":"t1109@163.com",
			"csrf_token":PHPwind.openIndex(self)
		}
		response4 = sesion_info.post(url='%s/phpwind/index.php?m=u&c=register&a=dorun'%host,
		                             data=register_info,
		                             headers = headers_info)
		print(response4.text)

	def doreply(self):
		reply_info = OrderedDict(
			[
				 ("atc_title",(None,'City18888888')),
				 ("atc_content",(None,'cityh回帖测试')),
				 ("pid",(None,'')),
				 ("tid",(None,89510)),
				 ("special",(None,'')),
				 ("reply_notice",(None,1)),
				 ("csrf_token",(None,PHPwind.openIndex(self)))
			         ]
		)
		response5 = sesion_info.post('%s/phpwind/index.php?c=post&a=doreply&_json=1&fid=68'%host,
		                             files= reply_info)

		print(response5.json())

	#cookies登录，并发帖
	def cookies_send_messege(self):
		messege_params = OrderedDict(
			[
				 ("atc_title",(None,'City of Stars6666')),
				 ("atc_content",(None,'request发帖打卡166666')),
				 ("pid",(None,'')),
				 ("tid",(None,'')),
				 ("special",(None,'default')),
				 ("reply_notice",(None,1)),
				 ("csrf_token",(None,PHPwind.openIndex(self)))
			         ]
		)
		response6 = sesion_info.post(url='%s/phpwind/index.php?c=post&a=doadd&_json=1&fid=57'%host,
		                             files= messege_params,
		                             cookies = PHPwind.Login2(self)
		                             )
		print(response6.json())


if __name__ =="__main__":
    php = PHPwind('test09',123456)
    php.openIndex()
    # php.Login1()
    # php.Login2()
    php.login_success()
    # php.send_messege()
    # php.register_id()
    # php.doreply()
    php.cookies_send_messege()