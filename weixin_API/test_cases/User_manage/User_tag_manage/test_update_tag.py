#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/16 17:34
# @File    : test_update_tag.py

# 编辑用户标签

import unittest
from weixin_API.common.start_end import StartEnd
from weixin_API.common.base import Base
from weixin_API.utils.log_utils import logger

class UpdateTag(StartEnd):

    @unittest.skipIf(True,'为真则跳过')
    def test_update_tag01_success(self):
        self._testMethodDoc = 'Case01'
        self._testMethodDoc = '验证修改标签成功'
        ramdonstr = Base().randomStr(5)
        token_id = Base().get_token()
        tag_id = Base().get_tag_id()
        print(tag_id)
        post_dict = {   "tag" : {     "id" : tag_id,     "name" : ramdonstr   } }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/update?access_token=%s'%token_id,
                                     json=post_dict)
        ascual_result = response.json()['errmsg']
        self.assertEqual(ascual_result,'ok','Case01 编辑标签成功')
        logger.info(response.json())



    @unittest.skipIf(True, '条件为真跳过')
    def test_create_tag02_Duplicate_Label(self):
        self._testMethodDoc = 'Case02'
        self._testMethodDoc = '验证编辑标签重复'
        post_dict = {   "tag" : {     "name" : 'H7HENu' } }
        token_id = Base().get_token()
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/update?access_token=%s'%token_id,
                                     json=post_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45157,'Case02 标签重复，编辑标签失败')
        logger.info(response.json())



    # @unittest.skipIf(True, '条件为真跳过')
    def test_update_tag03_default_tag(self):
        self._testMethodDoc = 'Case02'
        self._testMethodDoc = '验证不能修改0/1/2这三个系统默认保留的标签'
        ramdonstr = Base().randomStr(5)
        token_id = Base().get_token()
        post_dict = {   "tag" : {     "id" : 1,     "name" : ramdonstr   } }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/update?access_token=%s'%token_id,
                                     json=post_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45058,'Case02 不能修改0/1/2这三个系统默认保留的标签，编辑标签失败')
        logger.info(response.json())










if __name__ == '__main__':
    unittest.main()