#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 14:14
# @File    : test_data_readExcel_utils.py


# import os
# from weixin_API.utils.config_utils import config
# from weixin_API.utils.readExcel import ReadExcel
#
#
# class TeatDataUtils(object):
#     def __init__(self,test_data_type,test_data_excel_name,test_data_path = config.test_data_path):
#         data_path = os.path.join(os.path.dirname(__file__),test_data_path,test_data_excel_name+'.xlsx')
#         self.excel_data = ReadExcel(data_path).get_excel_data_by_list()
#
#     def get_test_case_data(self):
#         test_data_infos = {}
#         for i in range(0,len(self.excel_data)):
#             test_data_info = {}
#             test_data_info[]