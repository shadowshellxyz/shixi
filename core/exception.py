#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shadow
"""

class JarvisException(Exception):
    
    def __init__(self, code = "500", message = "Failure"):
        self.code = code
        self.message = message