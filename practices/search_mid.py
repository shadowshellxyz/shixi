#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shadow walker
"""

from tmpl.test_template import TestTemplate 

'''
二分查找
'''
class MidSearch(TestTemplate):

    def search(self, elements, target):
        left = 0
        right = len(elements) - 1
        while left <= right:
            mid = (int)((right - left) / 2) + left
            print('left=%s, right=%s, mid=%s' % (left, right, mid))
            if elements[mid] == target:
                return mid
            elif target < elements[mid]:
                right = mid -1
            else:
                left = mid + 1
        return -1
    
    def test0(self):
        # self.chars.insert(26, 'a')
        self.traverse(self.chars)
        result = self.search(self.chars, 'M')
        print(result)
        return

MidSearch().test()
