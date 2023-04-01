#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

import os
import configparser

import jd.api 

from common.util.logging.logger_factory import LoggerFactory
from common.util.model.paginator import Paginator

class BaseJdCpsOpenApi:

    domain = None
    port = None
    appkey = None
    secret = None
    logger = None

    def __init__(self):
        
        # 加载配置文件
        config = configparser.ConfigParser()
        config.read(os.getcwd() + '/conf/cps/jd/dev.ini')
        
        # 初始化配置项
        self.appkey = config.get('jd.union.openapi', 'appkey')
        self.secret = config.get('jd.union.openapi', 'secret')
        self.domain = config.get('jd.union.openapi', 'domain')
        self.port = config.get('jd.union.openapi', 'port')
        self.logger = LoggerFactory().get_logger()
        self.logger.debug(" %s %s %s %s" % (self.domain, self.port, self.appkey, self.secret))

        # OpenAPI 初始化 
        jd.setDefaultAppInfo(self.appkey, self.secret)

    def query(self, paginator: Paginator):
        try:
            is_continue = True
            while is_continue:
                try:
                    # 构建Request
                    request = self.build_query_request(paginator)
                    self.logger.debug("Paginator[page_index = %s, page_size = %s]" % (paginator.page_index, paginator.page_size))
                    
                    # 请求数据
                    response = self.query0(request)                   
                    # self.logger.debug(response)

                    # 更新分页参数
                    paginator.data_list = response
                    paginator.increment_page()
                    is_continue = paginator.has_next_page()
                except Exception as e:
                    print(e)
                    break
        except Exception as e: 
            print(e) 

    def build_query_request(self, paginator: Paginator):
        return None

    def query0(self, request):
        self.logger.debug("do nothing.")
        return None

        



