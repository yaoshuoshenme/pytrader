#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import pymysql
from pymysql import cursors

from common.Singleton import Singleton
from easytrader.utils.misc import file2dict
# from DBUtils.PooledDB import PooledDB, SharedDBConnection

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = CURRENT_PATH + "/config/mysql.json"

@Singleton
class DBConfig(object):
    def __init__(self):
        config = file2dict(CONFIG_PATH)
        self.host = config['host']
        self.port = config['port']
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']

    def get_connection(self):
        return pymysql.connect(host=self.host, port=self.port, db=self.database, user=self.user, passwd=self.password)

    def get_one(self, sql):
        con = self.get_connection()
        cursor = con.cursor(cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        con.close()
        return data

    def get_all(self, sql):
        con = self.get_connection()
        cursor = con.cursor(cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

    def update(self, sql):
        con = self.get_connection()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()

    def insert(self, sql):
        con = self.get_connection()
        cursor = con.cursor()
        cursor.execute(sql)
        id = cursor.lastrowid
        con.commit()
        cursor.close()
        con.close()
        return id


