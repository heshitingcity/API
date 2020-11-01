#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/16 18:55
# @File    : test_delete_tag.py


#删除标签

import unittest
from weixin_API.common.start_end import StartEnd
from weixin_API.common.base import Base
from weixin_API.utils.log_utils import logger


class DeleteTag(StartEnd):

    @unittest.skipIf(True,'为真则跳过')
    def test_delete_tag01_success(self):
        self._testMethodDoc = 'Case01'
        self._testMethodDoc = '验证删除标签成功'
        token_id = Base().get_token()
        tag_id   = Base().get_tag_id()
        post_dict = {   "tag":{        "id" : tag_id   } }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=%s'%token_id,
                                     json=post_dict)

        actual_result  = response.json()['errmsg']
        self.assertEqual(actual_result,'ok','删除标签成功')
        logger.info(response.json())




    @unittest.skipIf(True, '条件为真跳过')
    def test_delete_tag02_default_tag(self):
        self._testMethodDoc = 'Case02'
        self._testMethodDoc = '验证不能删除0/1/2这三个系统默认保留的标签'
        ramdonstr = Base().randomStr(5)
        token_id = Base().get_token()
        post_dict = {   "tag" : {     "id" : 1} }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=%s'%token_id,
                                     json=post_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45058,'Case02 不能删除0/1/2这三个系统默认保留的标签，删除标签失败')
        logger.info(response.json())







if __name__ == '__main__':
    unittest.main()