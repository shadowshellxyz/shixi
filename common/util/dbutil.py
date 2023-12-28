#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ShadowShell
"""
 
import pymysql

class DbUtil:

    connection = None

    def init(self):
        self.connection = pymysql.connect(host='localhost',
                     user='root',
                     password='SsWdMySQL',
                     database='shadowshell')
        
    def insert(self, sql): 
        connection = self.connection;
        try:
            connection.cursor().execute(sql)
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(e)
    

    def destroy(self):
        self.connection.close()