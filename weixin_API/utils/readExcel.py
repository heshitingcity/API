#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/15 14:15
# @File    : readExcel.py


import os
import xlrd
from weixin_API.utils.config_utils import config

class ReadExcel(object):
    def __init__(self,excel_path,sheet_name = None):
        self.excel_path =excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)

        return sheet

    @property
    def get_row_data(self):
        return self.sheet_data.nrows

    @property
    def get_col_data(self):
        return self.sheet_data.ncols

    def get_excel_data_by_list(self):
        all_excell_data = []
        for rownum in range(1,self.get_row_data):
            row_data = []
            for colnum in range(self.get_col_data):
                cell_value = self.sheet_data.cell_value(rownum,colnum)
                row_data.append(cell_value)
            all_excell_data.append(row_data)
        return all_excell_data

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__),config.test_data_path,'start_developent_case_data','login_case_data.xlsx')
    infos = ReadExcel(path).get_excel_data_by_list()
    print(infos)
