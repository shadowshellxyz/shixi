#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""

import time
import json

class StdBaseCoreModel:

    id = 0
    ext_info = {}
    status = ''
    env = ''
    creator_id = ''
    creator_name = ''
    gmt_create = None
    modifier_id = ''
    modifier_name = ''
    gmt_modified = None

    def init(self, id, ext_info, status, env, creator_id, creator_name, gmt_create, modifier_id, modifier_name, gmt_modified):
        self.id = id
        self.ext_info = ext_info
        self.status = status
        self.env = env
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.gmt_create = gmt_create
        self.modifier_id = modifier_id
        self.modifier_name = modifier_name
        self.gmt_modified = gmt_modified

    def build(self, status, env, creator_id, creator_name=''):
        self.status = status
        self.env = env
        self.creator_id = creator_id
        if creator_name == "":
            self.creator_name = self.creator_id
        else:
             self.creator_name = creator_name
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.gmt_create = now_time
        self.gmt_modified = self.gmt_create

    def to_string(self):
        return json.dumps(self.__dict__, ensure_ascii = False)
