#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shadow walker
"""

class Node:

    # id
    id = None

    # name
    name = None

    # children
    children = []

    def __init__(self, id, name = None, children = None):
        self.id = id
        self.name = name
        self.children = children

    def build_as_ids(self, ids):
        nodes = []
        for id in ids:
            nodes.append(Node(id))
        return nodes
    
    def build_as_dict(self, dict):
        return
    
    def to_string(self):
        return ('id=%s,name=%s' % (self.id, self.name))

class TestTemplate:

    chars = [
        'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X',
        'Y', 'Z'
    ]

    def __init__(self):
        return

    def test(self):

        try:
            self.console('-->> Ready')
            
            self.test0()

            self.console('-->> Do something')

        except Exception as e:
            self.console(e)
        except:
            self.console(sys.exc_info()[0])
        finally:
            self.console('-->> Done')
            return

    def test0(self):
        self.console('Nothing')
        return

    def console(self, content):
        print('[CONSOLE] %s' % (content))

    def traverse(self, elements):
        self.console('All elements : %s' % (elements))
