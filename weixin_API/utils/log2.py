#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/10/18  12:05
# @User : city
# @File : API  log2.py
# @Author : City


import os
import time
import win32com
from nb_log import LogManager
from weixin_API.utils.config_utils import config


log_name = os.path.join(os.path.dirname(__file__),config.logs_path,'API_test_%s.log'%time.strftime('%Y-%m-%d'))
logger = LogManager(log_name).get_logger_and_add_handlers()
logger.info('hhhh')