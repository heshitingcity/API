#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/9/20  9:57
# @User : city
# @File : API  demo01.py
# @Author : City


import requests
import json

'''
响应正文：  text格式、   json格式、  二进制格式、     原始格式

'''
#微信公众号平台--获取access_token
#方式一、response.content.decode('utf-8')   二进制响应
# requests.packages.urllib3.disable_warnings()
# response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx6245840484d8734b&secret=b2aa7a7874a77d1350f9822a53d838eb',verify=False)
# print(response.content.decode('utf-8'))

#方式二、  json方式
# get_token_dict= {"grant_type":"client_credential",
#                 "appid":"wx6245840484d8734b",
#                 "secret":"b2aa7a7874a77d1350f9822a53d838eb"
#
# }
# requests.packages.urllib3.disable_warnings()   #取消警告
# response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token?', params=get_token_dict,verify=False)
# print(response.content.decode('utf-8'))


# 方式三、get 请求头参数访问:
#请求头字典
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
#           }
# #在get请求内，添加user-agent
# response = requests.get(url='https://api.weixin.qq.com', headers=headers)
# print(response.status_code)  # 200
# # print(response.text)
# with open('zhihu.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)


#方式三 、post  请求
# requests.packages.urllib3.disable_warnings()   #取消警告
# url_params_dict = {"access_token":"37_Q7FdS1vC8NKLZ5lyimVuBhLOX2-xAOzsPCFwhafZiGlHtltTpt50R8kmE3p9jQmQ-1TN_wu0iH75MP_9SGFz_AX0z9KDGECFX2yMIS3Yx7uDJ5OGHiFLMakPGHjOnvGVslejKkkxBJ0PRKauXXWfAFAFFE"}
# post_param_data = {   "tag" : {     "name" : "12f访视"  } }
# response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?',
#                          params = url_params_dict ,
#                          data= json.dumps(post_param_data),
#                          verify=False
#
#
#                          )
# print(response.content.decode('utf-8'))


# response = requests.get(url='http://www.hnxmxit.com/')
# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.headers['Server'])
# print(response.headers['Content-Encoding'])
# print(response.text)    #响应文本
# print(response.content.decode('utf-8'))   #二进制响应内容


#方式四、 r.raw  查看原始响应内容




#01、下载图片
# from pil import image
# from io import BytesIO
# resonse = requests.get('',verify=False)
# img = image.open(BytesIO(resonse.content))
# img.save('../date/a.jpg')



#02、设置代理
# poxy_server = {'http':'http:127.0.0.1:8888',
#                'https':'http://127.0.0.1:8888'}
# response = requests.get(url='http://www.hnxmxit.com/',params=poxy_server,verify=False)
# print(response.status_code)

#03、超时异常:   公司里面用来检测系统间的心跳包
# import time
#
# print(time.time())
# requests.packages.urllib3.disable_warnings()
# response = requests.get(url='https://www.baidu.com',verify=False,timeout=10.001)
# print(time.time())


#04、重定向
# requests.packages.urllib3.disable_warnings()
# response = requests.get(url='http://www.360buy.com',verify=False)
# print(response.history)  #显示重定向历史
# print(response.url)
# print(response.content.decode('utf-8'))



#05、请求中添加cookie
# # 方式一、
# conkie_dict = {"company_name":"newdream"}
# requests.get(url='http://www.hnxmxit.com',verify=False,cookies = conkie_dict)
#
#
# #方式二、
# header_info_dict={
# 	"cookies"=="company_name":"newdream"
# }
# requests.get(url='http://www.hnxmxit.com',verify=False,cookies = header_info_dict)
#


#06、SSL认证报错
#解决方式一：
# verify=False  #  False：关闭证书认证
# requests.packages.urllib3.disable_warnings()  #取消警告


#解决方式二：安装pyopenssl
# pip install -U requests[security]

#解决方式二：加上证书
# response = requests.get(url='http://www.baidu.com',cert=('./path/server.crt','./path/key'))


#07、异常处理

#例子01、
# try:
# 	a = 10+ 'k'
# 	print(a)
# except TypeError as e:
# 	print('类型错误')


#例子02、
from requests.exceptions import *
try:
	response = requests.get(url='www.baidu.con')
except MissingSchema as e:
	print('url的错误')
except ConnectionError as e:
	print('链接超时')
except RequestException as e:
	print('请求异常')