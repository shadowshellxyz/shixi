#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shadow
"""

import sys
import os

class Shadow:

    # 私有属性
    DEFAULT_GREETING = "Hello"
    DEFAULT_END_COMMAND = "bye"

    # 构造函数
    def __init__(self, end_command = ""):
        print ("Initialization succeeded")

    # communicate
    def communicate(self):
        # 开始交流
        try:
            file = open("/Users/shadow/workbench/Shadow/总结与计划/TODOList.xlsx", "r")
            lines = file.readlines()
            keys = "retry|"
            index = 1
            length = len(lines)
            print(length)
            while index < length:
                items = lines[index].split(",")
                if index > 1:
                    keys = keys + ","
                keys = keys + "'"
                keys = keys + items[0].strip("\"")
                keys = keys + "'"
                index = index + 1
            print(keys)
        except Exception as e:
            self.__logger.error(e)
        except:
            self.__logger.error(sys.exc_info()[0])
        finally:
            # 关闭打开的文件
            file.close()
            return

    # destroy
    def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "Bye")

# 程序入口
shadow  = Shadow()
shadow.communicate()
