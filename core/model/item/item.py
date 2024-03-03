#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

from common.util.model.std_base_core_model import StdBaseCoreModel

class Item(StdBaseCoreModel):

    source = ''
    out_item_id = ''
    name = ''
    price = 0.00
    cid1_name = ''
    cid2_name = ''
    cid3_name = ''

    def build(self, source, out_item_id, name, price, cid1_name='', cid2_name='', cid3_name='', ext_info=''):
        # StdBaseCoreModel.build(self, 'ENABLED', 'DEV', 'shadowshell')
        self.source = source
        self.out_item_id = out_item_id
        self.name = name
        self.price = price
        self.cid1_name = cid1_name
        self.cid2_name = cid2_name
        self.cid3_name = cid3_name
        # StdBaseCoreModel.ext_info = ext_info


    
    

    
    

