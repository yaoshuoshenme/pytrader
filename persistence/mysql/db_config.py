#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from dbutils.pooled_db import PooledDB
from pymysql import cursors

from common.Singleton import Singleton
from easytrader.utils.misc import file2dict

CONFIG_PATH = os.path.join(os.getcwd(), 'account.json')
DB_POOL_CONFIG = {
    # 启动时开启的闲置连接数量(缺省值 0 开始时不创建连接)
    "min_cached": 5,
    # 连接池中允许的闲置的最多连接数量(缺省值 0 代表不闲置连接池大小)
    "max_cached": 1,
    # 共享连接数允许的最大数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量,被请求为共享的连接将会被共享使用
    "max_shared": 0,
    # 创建连接池的最大数量(缺省值 0 代表不限制)
    "max_connections": 20,
    # 设置在连接池达到最大数量时的行为
    "blocking": True,
    # 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用).当达到最大数时,连接会自动重新连接
    "max_usage": 0,
    # 一个可选的SQL命令列表用于准备每个会话
    "set_session": None,
    # 使用连接数据库的模块
    "creator": "pymysql"
}


@Singleton
class MyPooledDB(object):
    def __init__(self):
        config = file2dict(CONFIG_PATH)
        self.host = config['mysql']['host']
        self.port = config['mysql']['port']
        self.user = config['mysql']['user']
        self.password = config['mysql']['password']
        self.database = config['mysql']['database']

        self._pool = PooledDB(
            creator=DB_POOL_CONFIG['creator'],
            mincached=DB_POOL_CONFIG['min_cached'],
            maxcached=DB_POOL_CONFIG['max_cached'],
            maxshared=DB_POOL_CONFIG['max_shared'],
            maxconnections=DB_POOL_CONFIG['max_connections'],
            blocking=DB_POOL_CONFIG['blocking'],
            maxusage=DB_POOL_CONFIG['max_usage'],
            setsession=DB_POOL_CONFIG['set_session'],
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.database,
            use_unicode=False,
            charset='utf8'
        )

    def get_conn(self):
        conn = self._pool.connection()
        cursor = conn.cursor()
        return conn, cursor

    # 创建数据库连接conn和游标cursor
    def __enter__(self):
        self.conn, self.cursor = self.get_conn()

    # 释放连接池资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


@Singleton
class DBHelper(object):
    def __init__(self):
        self.poolDB = MyPooledDB()

    def get_one(self, sql):
        con, cursor = self.poolDB.get_conn()
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
