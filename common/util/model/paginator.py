#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Paginator(): 

    page_index = 1
    page_size = 10
    total_count = 0
    data_list = []

    def __init__(self, page_index = 1, page_size = 10):
        self.page_index = page_index
        self.page_size = page_size

    def has_next_page(self):
        if self.data_list == None:
            return False
        return len(self.data_list) >= self.page_size
    
    def increment_page(self):
        self.page_index = self.page_index + 1
    
    def to_string(self):
        return json.dumps(self.__dict__, ensure_ascii = False)

    