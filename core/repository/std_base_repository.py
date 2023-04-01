#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from common.util.logging.logger_factory import LoggerFactory
from core.repository.base_repository import BaseRepository

"""
@author: ShadowShell
"""
class StdBaseRepository(BaseRepository):

    __logger = LoggerFactory().get_logger()

    def save(self, record):
        self.get_logger().debug("save one record : %s." % record)

    def remove(self, id):
        self.get_logger().debug("remove one record : %s ." % id)

    def update(self, record):
        self.get_logger().debug("update one record : %s." % record)

    def query_by_id(self, id):
        self.get_logger().debug("query one record by id : %s." % id)
    
    def query_list(self, begin_index, page_size):
        self.get_logger().debug("query record list : %s, %s." % (begin_index, page_size))

    def get_logger(self):
        return self.__logger;
    