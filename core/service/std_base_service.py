#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

from common.util.logging.logger_factory import LoggerFactory

class StdBaseService():

    __logger = LoggerFactory().get_logger()

    def save(self, record):
        self.get_logger().debug("save one record : %s." % record)

    def remove(self, id):
        self.get_logger().debug("remove one record : %s ." % id)

    def update(self, record):
        self.get_logger().debug("update one record : %s." % record)

    def query_by_id(self, id):
        self.get_logger().debug("query one record by id : %s." % id)
    
    def query_list(self, id):
        self.get_logger().debug("query record list : %s." % id)

    def get_logger(self):
        return self.__logger;
    
    