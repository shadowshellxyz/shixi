#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shadow walker
"""

from tmpl.test_template import TestTemplate 

class List(TestTemplate):
    
    __list = []
    
    def __init__(self, elements):
        self.__list = list(elements)
        return

    def insert(self, index, element):
        self.__list.insert(index, element)
        return

    def pop(self, index):
        self.__list.pop(index)
        return

    def sort(self):
        self.__list.sort()
        
    def test0(self):
        self.traverse(self.__list)

        print(self.__list[0])

        self.insert(0, 'A')
        self.traverse(self.__list)

        self.pop(0)
        self.traverse(self.__list)

        print(self.__list[0:2])
        
        return

List(TestTemplate.chars).test()
