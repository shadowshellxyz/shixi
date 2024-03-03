#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

from core.service.std_base_service import StdBaseService

class ItemService(StdBaseService):
    

    def save(self, item):
        sql = "INSERT INTO item( \
              `source`, `out_item_id`, `name`, `cid1_name`, `cid2_name`, `cid3_name`, `price`, `ext_info`, `status`, `env`, `creator_id`, `creator_name`, `gmt_create`, `modifier_id`, `modifier_name`, `gmt_modified` \
                ) VALUES(\
                      '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                      (item.source, item.out_item_id, item.name, item.cid1_name, item.cid2_name, item.cid3_name, item.price, '', item.status, item.env, item.creator_id, item.creator_name, item.gmt_create, item.creator_id, item.creator_name, item.gmt_modified)
        
        self.logger.debug(sql)

        BaseService.save(self, sql)
