#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/9/20  17:02
# @User : city
# @File : API  demo02.py
# @Author : City

import re
import requests

#re   正则表达式模块
#实战001、
# requests 模拟 https://www.qq.com的请求，用re模块截取出
# <meta name="description" content="腾讯网从2003年创立至今，已经成为集新闻信息，区域垂直生活服务、社会化媒体资讯和产品为" \
#                                  "一体的互联网媒体平台。腾讯网下设新闻、科技、财经、娱乐、体育、汽车、时尚等多个频道，充分" \
#                                  "满足用户对不同类型资讯的需求。同时专注不同领域内容，打造精品栏目，并顺应技术发展趋势，推出" \
#                                  "网络直播等创新形式，改变了用户获取资讯的方式和习惯。" />中的content内容
#
# response = requests.get(url='https://www.qq.com/')
# # print(response.text)
# body = response.content.decode("gbk")  #使用uft-8报错，要根据网站的编码格式来选择使用
# # print(body)
# con = re.findall('name="description" content="(.+?)"',body)
# print( con )

#实战002、



#实战003、