#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

from core.util.dbutil import DbUtil
from core.util.logging.logger import LoggerFactory

class BaseService:

    logger = LoggerFactory().get_logger()
    dbUtil = None

    def __init__(self):
        self.dbUtil = DbUtil()
        self.dbUtil.init()

    def save(self, sql):
        self.dbUtil.insert(sql)
        


    