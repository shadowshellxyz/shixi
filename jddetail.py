#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""


from core.model.item.item import Item
from cps.jddetail import PriceService

priceService = PriceService()
priceService.get()

item = Item()
item.name = '测试商品'
print(item.name)
