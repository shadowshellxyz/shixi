#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shadow
"""

from .command.photo_archiving import PhotoArchiving
from .logging.logger import LoggerFactory

class Communication:


    # 构造函数
    def __init__(self, end_command = "byebye"):
        # 初始化日志
        self.__logger = LoggerFactory().get_logger()
        self.__end_command = end_command

    # communicate
    def communicate(self, command = "Hello"):
        try:
            while command == self.__end_command:
                self.__logger.info("Bye bye.")
                break
            else:
                self.__logger.debug("Responsing for the command '%s'." % (command))
                self.__response(command)
                self.__logger.debug("Success to response for the command '%s'." % (command))
                self.communicate(command = input())
        except Exception as e:
            self.__logger.error(e)
        except:
            self.__logger.error(sys.exc_info()[0])
        finally:
            return
            
    # response
    def __response(self, command):
        if command == "":
            self.__response_for_invalid_command(command)
        else:
            if command == "Hello":
                self.__logger.info("Hi.")
            else:
                commandItems = command.split(" ")
                if commandItems[0] == "archive":
                    command_handler = PhotoArchiving()
                    self.__logger.info("Found a command handler '%s'." % (command_handler))
                    command_handler.archive()
                else:
                    self.__response_for_invalid_command(command)
        return

    def __response_for_invalid_command(self, command):
        self.__logger.info("Invalid command:'%s', please input retry." % (command))