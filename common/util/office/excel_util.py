#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip3 install xlrd==1.2.0

@author: Shadow
"""

import xlrd
import openpyxl

class ExcelUtil:

    # 读取数据
    def read(self, file_path):
        # 打开execl
        workbook = xlrd.open_workbook(file_path)
        # 输出excel文件中所有sheet的名字
        print(workbook.sheet_names())
        # 通过索引获取
        data_sheet = workbook.sheets()[0] 
        # data_sheet = workbook.sheet_by_index(0) # 通过索引获取
        # data_sheet = workbook.sheet_by_name(u'名称') # 通过名称获取
        print(data_sheet.name) # 获取sheet名称
        # 获取所有单元格的内容
        list = []
        for row_index in range(data_sheet.nrows):
            rowlist = []
            for col_index in range(data_sheet.ncols):
                #print(data_sheet.cell_value(row_index, col_index))
                rowlist.append(data_sheet.cell_value(row_index, col_index))
            list.append(rowlist)
        return list
    
    def read2(self):
        prompt_msg = "please input your file path : "
        file_path = input(prompt_msg)
        while file_path == None:
            input(prompt_msg)
        self.read(file_path)
        return 

    # 输出数据
    def write(self, data, file_path, title):
        # 创建工作簿
        workbook = openpyxl.Workbook()
        # 创建sheet
        data_sheet = workbook.active
        data_sheet.title = title
        # 写入数据
        for row_index in range(len(data)):
            for col_index in range(len(data[row_index])):
                data_sheet.cell(row_index + 1, col_index + 1, data[row_index][col_index])
        # 保存文件
        workbook.save(file_path)


