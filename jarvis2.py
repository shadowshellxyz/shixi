#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shadow
"""

import sys
import os
from core.communication import Communication
from core.logging.logger import LoggerFactory
from core.exception import JarvisException

# from core.exception import JarvisException

class Jarvis:

    # 私有属性
    DEFAULT_GREETING = "Hello"
    DEFAULT_END_COMMAND = "bye"

    # 构造函数
    def __init__(self, end_command = ""):
        # 初始化日志
        self.__logger = LoggerFactory().get_logger()
        # 初始化配置信息
        self.__initConfs()
        # 初始化结束命令
        if end_command != "":
            self.__end_command = end_command
        self.__logger.info("End command is '%s'." % (self.__end_command))
        self.__logger.info("Greeting command is '%s'." % (self.__greeting))
        # 实例化Communication
        self.__communication = Communication(self.__end_command)

    # communicate
    def communicate(self):
        # 开始交流
        try:    
            self.__logger.info("Communicating, command is '%s'." % (self.__greeting))
            self.__communication.communicate(self.__greeting)
            self.__logger.info("Communication is end")
        except JarvisException as e:
            self.__logger.error(e)
        except Exception as e:
            self.__logger.error(e)
        except:
            self.__logger.error(sys.exc_info()[0])
        finally:
            return
    
    # 初始化配置信息
    def __initConfs(self):
        try:
            self.__logger.info("Loading configurations.")
            confs = self.__read_confs()
            # 初始化问候语配置
            self.__init_greeting_conf(confs)
            # 初始化结束命令配置
            self.__init_end_command_conf(confs)
            self.__logger.info("Loaded configurations.")
            return
        except Exception as e:
            self.__logger.error(e)

    # 读取配置信息
    def __read_confs(self):
        # 当前路径
        current_path = os.getcwd()
        # 配置文件路径
        conf_path = current_path + "/conf/jarvis.conf"
        self.__logger.info("Configuration file path is '%s'." % (conf_path))
        # 加载配置文件
        conf_file = open(conf_path, "r", encoding="utf-8")
        confs = conf_file.readlines()
        conf_file.close()
        return confs

    # 初始化问候语配置
    def __init_greeting_conf(self, confs):
        # 问候语
        greeting = confs[0].split("=")[1]
        self.__logger.info("Loaded configuration, key is 'greeting', value is '%s'." % (greeting))
        if greeting == "":
            self.__greeting = DEFAULT_GREETING
        else:
            self.__greeting = greeting

    # 初始化结束命令配置
    def __init_end_command_conf(self, confs):
        end_command = confs[1].split("=")[1]
        self.__logger.info("Loaded configuration, key is 'endcommand', value is '%s'." % (end_command))
        if end_command == "":
            self.__end_command = DEFAULT_END_COMMAND
        else:
            self.__end_command = end_command

# 程序入口
jarvis  = Jarvis()
jarvis.communicate()
