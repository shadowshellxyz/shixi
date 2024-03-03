#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shadow walker
"""

from tmpl.test_template import TestTemplate, Node

class Tree(TestTemplate):

    root = Node('root')

    def visit(self, nodes):
        if nodes == None:
            return
        for node in nodes:   
            self.console(node.to_string())
            self.visit(node.children)
        return

tree = Tree()
tree.root.children = Node('').build_as_ids(TestTemplate.chars)
tree.visit([(tree.root)])