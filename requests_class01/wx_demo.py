#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/9/20  16:37
# @User : city
# @File : API  wx_demo.py
# @Author : City


import requests
import jsonpath



host = 'https://api.weixin.qq.com'

#01、获取token
get_param_dict= {
				"grant_type":"client_credential",
                "appid":"wx6245840484d8734b",
                "secret":"b2aa7a7874a77d1350f9822a53d838eb"
}
response = requests.get(url='%s/cgi-bin/token'%host,params=get_param_dict)
json_object = response.json()
token = jsonpath.jsonpath(json_object,'$.access_token')[0]  #关联token


#02、新建标签
get_token_dict = { "access_token":token }
post_data= {"tag" : {     "name" : "广东214235"   }}
response1 = requests.post(url='%s/cgi-bin/tags/create'%host,
                          params=get_token_dict,
                          json=post_data)
json_object1 = response1.json()
create_tag_id = jsonpath.jsonpath(json_object1,'$.tag.id')  #关联tag_id
print(create_tag_id)

#03、编辑标签
response2 = requests.post(url='%s//cgi-bin/tags/update'%host,
                          json={   "tag" : {     "id" : create_tag_id,     "name" : "123ssss"   } })


#04、查看标签
response3 = requests.get(url='%s/cgi-bin/tags/get'%host,
                         params=get_token_dict)
all_tag = response3.json()
print(all_tag)

#05、删除标签

response4 = requests.post(url='%s/cgi-bin/tags/delete'%host,
                          params=get_token_dict,
                          json={   "tag":{        "id" : create_tag_id   } }
                          )

