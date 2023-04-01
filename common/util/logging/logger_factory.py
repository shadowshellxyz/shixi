#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LoggerFactory
@author: ShadowShell
"""

from common.util.logging.adapter.console_logger import ConsoleLogger

class LoggerFactory:
        
    logger = None

    def __init__(self):
        self.logger = ConsoleLogger()

    def get_logger(self, name = "default"):
        return self.logger