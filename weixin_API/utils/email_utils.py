#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/10/18  14:40
# @User : city
# @File : API  email_utils.py
# @Author : City

from weixin_API.utils.config_utils import config


class EmailUtils:
	def __init__(self,sttp_body,smtp_path=None):
		self.smt_sender = config.receiver
		self.sender = config.sender
		self.smtp_password = config.SMTP_code
		