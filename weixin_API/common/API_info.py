#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time : 2020/10/18  9:14
# @User : city
# @File : API  API_info.py
# @Author : City

import requests
import unittest
from weixin_API.utils.config_utils import config
from weixin_API.utils.log_utils import logger




class API:
	session = requests.session()
	def get_access_token(self,appid,secret):
		get_param_dict = {
			"grant_type": "client_credential",
			"appid": appid,
			"secret": secret
		}
		try:
			response = self.session.get(url='https://%s/cgi-bin/token' % config.Host,
			                            params=get_param_dict)
		except Exception as e :
			logger.debug(e)
		return response

	def get_access_token_default_value(self):
		response = self.get_access_token('wx6245840484d8734b','b2aa7a7874a77d1350f9822a53d838eb')
		return response


	def get_access_token_value(self,appid,secret):
		response = self.get_access_token(appid,secret)
		return response


if __name__ == '__main__':
	unittest.main()