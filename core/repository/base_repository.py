#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.util.dbutil import DbUtil

"""
@author: ShadowShell
"""
class BaseRepository:

    dbUtil = None

    def __init__(self):
        self.dbUtil = DbUtil()
        self.dbUtil.init()

    def save(self, sql):
        self.dbUtil.insert(sql)

    def save(self):
        print("save")
    
    