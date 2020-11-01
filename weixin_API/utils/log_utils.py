#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 10:51
# @File    : log_utils.py

import os
import time
import logging
from logging import handlers
from weixin_API.utils.config_utils import config




class Mylog(object):
    def __init__(self,logger = None):
        self.log_name = os.path.join(os.path.dirname(__file__),config.logs_path,'API_test_%s.log'%time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger(logger)  #创建日志对象
        self.logger.setLevel(config.log_level)


        self.sh = handlers.TimedRotatingFileHandler(self.log_name, when='D', interval=1, backupCount=7 )
        self.sh = logging.FileHandler(self.log_name,'a',encoding='utf-8')


        self.ch = logging.StreamHandler()
        self.sh.setLevel(config.log_level)
        self.ch.setLevel(config.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
        )
        self.sh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.ch)
        self.sh.close()
        self.ch.close()

    def get_log(self):
        return self.logger






logger = Mylog().get_log()

if __name__ == '__main__':
    logger.info('dsjlf')



