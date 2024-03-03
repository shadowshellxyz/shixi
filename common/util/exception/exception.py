#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: shadow walker
"""

class AppException(Exception):

    code = ""
    message = ""
    
    def __init__(self, code = "500", message = "Failure"):
        self.code = code
        self.message = message