#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip3 install xlrd==1.2.0

@author: Shadow
"""

import xlrd

from base import BaseCommand

class Command(BaseCommand):

    def execute(self):
        prompt_msg = "please input your file path : "
        file_path = input(prompt_msg)
        while file_path == None:
            input(prompt_msg)
        # 打开execl
        workbook = xlrd.open_workbook(file_path)
        # 输出excel文件中所有sheet的名字
        # print(workbook.sheet_names())
        # 通过索引获取
        data_sheet = workbook.sheets()[0] 
        # data_sheet = workbook.sheet_by_index(0) # 通过索引获取
        # data_sheet = workbook.sheet_by_name(u'名称') # 通过名称获取
        # print(data_sheet.name) # 获取sheet名称
        # 获取所有单元格的内容
        list = []
        col_names = ""
        for col_index in range(data_sheet.ncols):
                col_names = col_names + data_sheet.cell_value(0, col_index) + "||"
        print(col_names)
        for row_index in range(data_sheet.nrows):
            if row_index == 0:
                continue
            rowlist = []
            row_values = ""
            for col_index in range(data_sheet.ncols):
                rowlist.append(data_sheet.cell_value(row_index, col_index))
                row_values = row_values + data_sheet.cell_value(row_index, col_index) + "||"
            print(row_values)
            list.append(rowlist)
        return list

if __name__ == '__main__':
    command = Command()
    command.execute()

