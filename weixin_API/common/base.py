#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/16 16:33
# @File    : base.py


import unittest
import time
import os
import random
import string
import yaml
from weixin_API.utils.log_utils import logger
from weixin_API.utils.config_utils import config

class Base(object):

    def randomStr(self,randomLength):
        str_list = [random.choice(string.digits+string.ascii_letters) for i in range(randomLength)]
        random_str = ''.join(str_list)
        return random_str

    def get_token(yamlName = "Token.yaml"):
        path = os.path.join(os.path.dirname(__file__),config.yamal_path)
        f = open(path)
        a = f.read()
        token = yaml.load(a, Loader=yaml.FullLoader)
        f.close()
        return token['access_token']


    def get_tag_id(yamal = "Token.yaml"):
        path = os.path.join(os.path.dirname(__file__),config.yamal_path)
        f = open(path)
        tag_id = yaml.load(f.read(),Loader=yaml.FullLoader)
        return tag_id['tag']['id']


if __name__ == '__main__':
    unittest.main()