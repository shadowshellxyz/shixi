#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LoggerFactory
@author: shadow walker
"""
class Logger:

    def debug(self, content):
        self.__log(content)
        
    def info(self, content):
        self.__log(content)

    def warn(self, content):
        self.__log(content)
    
    def error(self, content):
        self.__log(content)

    def __log(self, content):
        print("[LOGGER]%s" % content)

# """
# LoggerFactory
# @author: ShadowShell
# """

# import os

# class LoggerFactory:

#     def __init__(self):
#         current_path = os.getcwd()
#         conf_file_path = current_path + "/conf/logging.yaml"
#         log_file_path = os.path.join(current_path, 'logs')
#         self.__conf_file_path = conf_file_path
#         self.__log_file_path = log_file_path
#         self.__log("conf_file_path=" + self.__conf_file_path)
#         self.__log("log_file_path=" + self.__log_file_path)
        
#     def get_logger(self, logger_name = "default"):
#         logger = Logger(self.__conf_file_path, self.__log_file_path)
#         return logger.get_logger(logger_name)
    
#     def __log(self, content):
#         print("LoggerFactory->" + content)


# """
# Logger
# @author: Shadow
# """
# import logging
# import logging.config
# import os
# import yaml

# class Logger:

#     def __init__(self, conf_file_path, log_file_path):
#         # 检查日志输出路径，没有则创建
#         if not os.path.exists(os.path.dirname(log_file_path)):
#             os.makedirs(os.path.dirname(log_file_path))
#         # 打开日志配置文件
#         with open(conf_file_path, "r") as conf_file:
#             logging_config = yaml.safe_load(conf_file)
#         # 补全日志输出路径
#         if log_file_path is not None:
#             log_file_name = logging_config['handlers']['default']['filename']
#             self.__log("log_file_name=" + log_file_name)
#             # logging_config['handlers']['default']['filename'] = os.path.join(log_file_path, log_file_name)
#         # 设置日志配置
#         logging.config.dictConfig(logging_config)
#         return

#     def get_logger(self, logger_name):
#         return logging.getLogger(logger_name)

#     def debug(self, content):
#         return
        
#     def info(self, content):
#         print(content)
#         return

#     def warning(self, content):
#         return
    
#     def error(self, content):
#         return

#     def __log(self, content):
#         print("Logger->" + content)
    