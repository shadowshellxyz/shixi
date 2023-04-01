#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

import json 

import jd.api 
from jd.api.rest.UnionOpenGoodsBigfieldQueryRequest import UnionOpenGoodsBigfieldQueryRequest 
from core.model.item.item import Item

from biz.cps.cps_item_service import CpsItemService
from biz.cps.jd.base_jd_cps_open_api import BaseJdCpsOpenApi


class JdCpsItemService(CpsItemService, BaseJdCpsOpenApi):

    def query_by_id(self, id):
        req = UnionOpenGoodsBigfieldQueryRequest(self.domain, self.port) 
        req.goodsReq={"skuIds": [id]}
        req.version = "1.0" 
        res = req.getResponse("")
        result = res['jd_union_open_goods_bigfield_query_response']['queryResult']
        biz_data = json.loads(result)
        out_item = biz_data['data']['bigFieldGoodsResp']
        self.get_logger().debug(out_item['skuName'])
        self.get_logger().debug("id -->> %s" % id)
