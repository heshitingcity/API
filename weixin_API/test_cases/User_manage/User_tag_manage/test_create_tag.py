#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 19:29
# @File    : test_create_tag.py

# 创建用户标签

import os
import unittest
from weixin_API.common.start_end import StartEnd
from weixin_API.utils.log_utils import logger
from weixin_API.common.base import Base
from weixin_API.utils.config_utils import config
from ruamel import yaml



class CreatTag(StartEnd):

    @unittest.skipIf(False, '条件为真跳过')
    def test_create_tag01_success(self):
        self._testMethodDoc = 'Case01 '
        self._testMethodDoc = '验证创建标签接口调用成功'
        random1 = Base().randomStr(6)
        post_dict = {   "tag" : {     "name" : random1 } }
        token_id = Base().get_token()
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     json=post_dict)

        actual_result = response.json()['tag']['name']
        self.assertEqual(actual_result,random1,'case01 验证create_tag接口能否成功调用')
        logger.info(response.json())

        yamlpath = os.path.join(os.path.dirname(__file__),'../../',config.yamal_path)
        print(yamlpath)
        tag_id =response.json()
        with open(yamlpath,'a',encoding='utf-8') as f:
            yaml.dump(tag_id,f,Dumper=yaml.RoundTripDumper)


    @unittest.skipIf(True, '条件为真跳过')
    def test_create_tag02_Duplicate_Label(self):
        self._testMethodDoc = 'Case02'
        self._testMethodDoc = '验证创建标签重复'
        post_dict = {   "tag" : {     "name" : 'H7HENu' } }
        token_id = Base().get_token()
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     json=post_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45157,'Case02 标签重复，创建标签失败')
        logger.info(response.json())

    @unittest.skipIf(True, '条件为真跳过')
    def test_create_tag03_longTagName(self):
        self._testMethodDoc = 'Case03'
        self._testMethodDoc = '标签名长度超过30个字节,标签创建失败'
        random1 = Base().randomStr(31)
        post_dict = {   "tag" : {     "name" : random1 } }
        token_id =  Base().get_token()
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     json=post_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45158,'case03 标签名长度超过30个字节,标签创建失败')
        logger.info(response.json())



    @unittest.skipIf(True,'条件为真跳过')
    def test_create_tag04_Tag_More_than_100(self):
        self._testMethodDoc = 'Case04'
        self._testMethodDoc = '创建的标签数过多，超过100'
        random1 = Base().randomStr(31)
        post_dict = {"tag": {"name": random1}}
        token_id =  Base().get_token()
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s' % token_id,
                                     json=post_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result, 45056, 'case04 创建的标签数过多，超过100,标签创建失败')
        logger.info(response.json())








if __name__ == '__main__':
    unittest.main()