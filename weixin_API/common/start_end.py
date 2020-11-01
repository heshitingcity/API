#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 10:37
# @File    : start_end.py


import unittest
import requests
from weixin_API.utils.config_utils import config



class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.host = config.Host


    def tearDown(self) -> None:
        self.session.close()