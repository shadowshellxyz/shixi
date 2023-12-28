#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shadow
"""

from core.office.excel_util import ExcelUtil

excel_util = ExcelUtil()
# list = excel_util.read('/Users/shadow/workbench/Shadow/总结与计划/TODOList.xlsx')
# for i in range(len(list)):
#     row = ''
#     for j in range(len(list[i])):
#         col_value = str(list[i][j])
#         row = row + col_value
#     print(row)

data = [['id', 'name'], ['shadow', '影']]
excel_util.write(data, '/Users/shadow/Desktop/test.xlsx', 'test')
