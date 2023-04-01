#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from common.util.exception.exception import AppException
from common.util.logging.logger_factory import LoggerFactory

from core.model.item.item import Item
from core.model.item.price import Price
from biz.cps.jd.jd_cps_item_service import JdCpsItemService

class Test():

    logger = None;

    def __init__(self):
        self.logger = LoggerFactory.get_logger(self)

    def test_item(self):

        price = Price()
        price.item_id = '0001'
        print(price.item_id)

        item = Item()
        item.name = '测试商品'
        print(item.name)

        item_service = JdCpsItemService();
        item_service.query_by_id("31218153471");

    def test(self):
        
        try:    
            self.test_item()
        # except AppException as e:
        #     self.logger.error(e)
        # except Exception as e:
        #     self.logger.error(e)
        except:
            # self.logger.error(sys.exc_info()[0])
            print(sys.exc_info())
            raise
        finally:
            return
        

test = Test()
test.test()
