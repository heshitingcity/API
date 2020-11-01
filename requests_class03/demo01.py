#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/10/11  9:33
# @User : city
# @File : API  demo01.py
# @Author : City


import requests

#一、获取cookies信息
# session_info = requests.session()


#方式1、
# session_info.cookies['company_name']='newdream'
# response = session_info.get(url='http://47.107.178.45/phpwind')
#
# #方式2、
# session_info.cookies.set('company_name','newdream',path='/')
# response = session_info.get(url='http://47.107.178.45/phpwind')

#方式3、
# cookies_dict =


#方式4、


#二、re模块
import re

#原字符 、 量词 的配合使用

str1 = '123a13dFsk123fsFeiFeEnedkhello'
result = re.match('1\d3',str1).group()
print(result)

value = re.match( 'class\d8' , 'class58' ).group()    #  match  \d:
print( value )

value1 = re.search('fs\w+',str1).group()    # search   \w
print(value1)

value2 = re.split('\d',str1)   # split
print(value2)

value3 = re.findall('fs\w+e',str1)
print(value3)


#迭代器:
value4 = re.finditer('fs\w+',str1)   #以字符串形式返回str1中的所有非重叠匹配项
for v in value4:
	print(v.group())


#替换
# value5 = re.sub('(\w+ )(\w+),r'fs\d',str1)