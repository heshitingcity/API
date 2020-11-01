#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 10:36
# @File    : test_get_access_token.py


import unittest
import time
import requests
import os
from weixin_API.utils.config_utils import config
from weixin_API.utils.log_utils import logger
from weixin_API.common.start_end import StartEnd
from unittestreport import TestRunner
from ruamel import yaml
from weixin_API.common.API_info import API


class GetAccessTokenAction(StartEnd):
    # session = requests.session()


    @unittest.skipIf(False, '条件为真跳过')
    def test_get_access_token01_success(self):
        self._testMethodDoc = '验证token_success接口成功调用'
        response = API().get_access_token_default_value()
        actual_result = response.status_code
        self.assertEqual(actual_result,200,'case01 ： 获取access_token接口调用成功！')
        yamlpath = os.path.join(os.path.dirname(__file__),'..',config.yamal_path)
        access_token =response.json()
        logger.info(access_token)
        with open(yamlpath,'w+',encoding='utf-8') as f:
            yaml.dump(access_token,f,Dumper=yaml.RoundTripDumper)


    @unittest.skipIf(False, '条件为真跳过')
    def test_get_access_token02_error_appid(self):
        self._testMethodDoc = '验证appid错误，access_token获取失败'
        response = API().get_access_token_value("wx6245840484d8734b1111","b2aa7a7874a77d1350f9822a53d838eb")
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40013,'case02 ： 获取access_token接口调用失败！')
        logger.info(actual_result)



    @unittest.skipIf(False, '条件为真跳过')
    def test_get_access_token03_error_secret(self):
        self._testMethodDoc = '验证asecret错误，access_token获取失败'
        response = API().get_access_token_value("wx6245840484d8734b", "b2aa7a7874a7b")
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40125,'case03 ： 获取access_token接口调用失败！')
        logger.info(actual_result)







if __name__ == '__main__':
    # unittest.main()
    reportpath = os.path.join(os.path.dirname(__file__),'../',config.report_path).replace('\\','/')
    reportName = 'GetAccessToken_API_%s'%time.strftime('%Y-%m-%d')
    suite = unittest.defaultTestLoader.discover(
                                                start_dir= '',
                                                pattern='test_get_access_token.py',
                                                top_level_dir=None
    )
    runner = TestRunner(
                        suite,
                        filename=reportName,
                        report_dir=reportpath,
                        title= '微信自动化接口测试报告',
                        tester= 'city',
                        templates= 2
    )
    runner.run()