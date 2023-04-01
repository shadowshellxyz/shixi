#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json 

from jd.api.rest.UnionOpenGoodsBigfieldQueryRequest import UnionOpenGoodsBigfieldQueryRequest 
from jd.api.rest.UnionOpenGoodsJingfenQueryRequest import UnionOpenGoodsJingfenQueryRequest

from common.util.model.paginator import Paginator
from core.model.item.item import Item
from biz.cps.cps_item_service import CpsItemService
from biz.cps.jd.base_jd_cps_open_api import BaseJdCpsOpenApi

"""
@author: ShadowShell
"""
class JdCpsItemService(CpsItemService, BaseJdCpsOpenApi):

    def query_by_id(self, id):
        req = UnionOpenGoodsBigfieldQueryRequest(self.domain, self.port) 
        req.goodsReq={"skuIds": [id]}
        req.version = "1.0" 
        res = req.getResponse("")
        result = res['jd_union_open_goods_bigfield_query_response']['queryResult']
        biz_data = json.loads(result)
        out_item = biz_data['data']['bigFieldGoodsResp']
        # self.get_logger().debug(out_item['skuName'])
        self.get_logger().debug("id -->> %s" % id)

    def query_list(self, begin_index = 1, page_size = 10):
        paginator = Paginator(begin_index, page_size)
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
        request = UnionOpenGoodsJingfenQueryRequest(self.domain, self.port) 
        request.goodsReq = {"eliteId": 1, "pageIndex": paginator.page_index, "pageSize": paginator.page_size} 
        request.version = "1.0" 
        return request

    def query0(self, request):
        response = request.getResponse("")
        result = response['jd_union_open_goods_jingfen_query_responce']['queryResult']
        bizData = json.loads(result)
        out_items = bizData['data']
        for out_item in out_items:
            categoryInfo = out_item['categoryInfo']
            item = Item()
            item.build('JD', out_item['skuId'], out_item['skuName'], out_item['priceInfo']['price'], categoryInfo['cid1Name'], categoryInfo['cid2Name'], categoryInfo['cid3Name'],)
            self.get_logger().debug(item.to_string())


            # item_service.save(item)
        return out_items