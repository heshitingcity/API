#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 10:20
# @File    : config_utils.py




import os
import configparser


conf_path = os.path.join(os.path.dirname(__file__),'../config/config_infos')


class ConfigUtils:
    def __init__(self,conf_path=conf_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(conf_path,encoding='utf-8')


    @property
    def Host(self):
        value = self.cfg.get('default','host')
        return value

    @property
    def report_path(self):
        value = self.cfg.get('default','report_path')
        return value

    @property
    def logs_path(self):
        value = self.cfg.get('default','logs_path')
        return value


    @property
    def log_level(self):
        value = int(self.cfg.get('default','log_level'))
        return value

    @property
    def test_data_path(self):
        value = self.cfg.get('default','test_data_path')
        return value


    @property
    def yamal_path(self):
        value = self.cfg.get('default','yamal_path')
        return value



    @property
    def receiver(self):
        value = self.cfg.get('email','receiver')
        return value


    @property
    def sender(self):
        value = self.cfg.get('email','sender')
        return value


    @property
    def SMTP_cs(self):
        value = self.cfg.get('email','SMTP_cs')
        return value

    @property
    def SMTP_subject(self):
        value = self.cfg.get('email','SMTP_subject')
        return value


    @property
    def SMTP_attch_path(self):
        value = self.cfg.get('email','SMTP_attch_path')
        return value


    @property
    def SMTP_port(self):
        value = self.cfg.get('email','SMTP_port')
        return value

    @property
    def SMTP_code(self):
        value = self.cfg.get('email','SMTP_code')
        return value

config = ConfigUtils()

if __name__ == '__main__':
    print(config.Host)
    print(config.report_path)
    print(config.logs_path)
    print(config.log_level)
    print(config.test_data_path)
    print(config.receiver)