#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shadow
"""

import openpyxl

from base import BaseCommand

class Command(BaseCommand):

    # 输出数据
    def execute(self):
        print("dddd")
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

if __name__ == '__main__':
    command = Command()
    command.execute()