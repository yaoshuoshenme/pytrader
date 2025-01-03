#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dataclasses import dataclass
from persistence.mysql.db_config import *
from common.Singleton import Singleton


class DBModel:
    def flush(self):
        pass


@dataclass
class Balance(DBModel):
    """
    账户
    """

    id: int
    name: str
    # 总资产
    asset_balance: float
    # 当前资金
    current_balance: float
    # 可用资金
    enable_balance: float
    # 冻结资金
    frozen_balance: float
    # 持仓市值
    market_value: float

    def update(self, market_value, current_balance):
        self.market_value = market_value
        self.current_balance = current_balance
        self.asset_balance = self.current_balance + self.market_value

    def update_total(self):
        self.asset_balance = self.current_balance + self.market_value

    def flush(self):
        sql = "update balance set asset_balance = %s, current_balance = %s, enable_balance = %s, frozen_balance = %s," \
              "market_value = %s where id = %d" % (
              str(self.asset_balance), str(self.current_balance), str(self.enable_balance),
              str(self.frozen_balance), str(self.market_value), self.id)
        DBHelper().update(sql)

    def _insert_db(self, name='default', asset_balance=1000000):
        sql = "insert into balance (`name`, `asset_balance`) values ('%s', '%s')" % (name, asset_balance)
        self.id = DBHelper().insert(sql)


@dataclass
class Position(DBModel):
    """
    持仓
    """
    # 账户id
    balance_id: int

    id: int
    # 当前持仓总数量
    current_amount: int
    # 可卖数量
    enable_amount: int
    # 资金收益
    income_balance: int
    # 成本价
    cost_price: float
    # 最新价
    last_price: float
    # 市值
    market_value: float
    # 股票代码
    stock_code: str
    # 股票名称
    stock_name: str
    # 状态, 1有效，0无效
    status: int = 1

    def __init__(self, balance_id, current_amount, cost_price, last_price, market_value,
                 stock_code, stock_name, enable_amount=0, income_balance=0, status=1):
        self.balance_id = balance_id
        self.current_amount = current_amount
        self.enable_amount = enable_amount
        self.income_balance = income_balance
        self.cost_price = cost_price
        self.last_price = last_price
        self.market_value = market_value
        self.stock_code = stock_code
        self.stock_name = stock_name
        self.status = status

    def update(self, last_price: float):
        self.last_price = last_price
        self.market_value = self.current_amount * last_price

    def flush(self):
        if self.id:
            sql = "update `position` set current_amount = %s, enable_amount = %s, income_balance = %s, cost_price = %s," \
                  "last_price = %s, market_value = %s, status = %d where id = %d" % (
                      str(self.current_amount), str(self.enable_amount), str(self.income_balance),
                      str(self.cost_price), str(self.last_price), str(self.market_value), self.status, self.id)
            DBHelper().update(sql)
        else:
            sql = "insert into `position` (balance_id, current_amount, enable_amount,income_balance, cost_price, last_price," \
                  "market_value, stock_code, stock_name, status) values (%d, %d, %d, '%s','%s','%s','%s','%s','%s',,%d)" % (
                      self.balance_id, self.current_amount, self.enable_amount, str(self.income_balance),
                      str(self.cost_price),
                      str(self.last_price), str(self.market_value), self.stock_code, self.stock_name, self.status
                  )
            self.id = DBHelper().insert(sql)


@dataclass
class Entrust(DBModel):
    """
    历史委托
    """

    # 账户id
    balance_id: int

    # 委托单号
    entrust_no: str
    # 买卖类别
    bs_type: str
    # 委托数量
    entrust_amount: int
    # 委托价格
    entrust_price: float
    # 委托上报时间
    report_time: str
    # 委托状态
    entrust_status: str
    # 股票代码
    stock_code: str
    # 股票名称
    stock_name: str
    # 费用
    cost: float

    def flush(self):
        db = DBHelper()
        query_sql = "select entrust_no from entrust where entrust_no = '%s'" % self.entrust_no
        data = db.get_one(query_sql)
        if data:
            sql = "update `entrust` set entrust_status = %s where entrust_no = %s" % (
            self.entrust_status, self.entrust_status)
        else:
            sql = "insert into entrust (balance_id, entrust_no, bs_type, entrust_amount, entrust_price, report_time," \
                  "entrust_status, stock_code, stock_name,cost) values (%d, '%s', '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s')" % (
                      self.balance_id, self.entrust_no, self.bs_type, self.entrust_amount, str(self.entrust_price),
                      self.report_time,
                      self.entrust_status, self.stock_code, self.stock_name, str(self.cost)
                  )
        db.update(sql)


@Singleton
@dataclass
class PerTrade:
    """
    交易费用
    """
    # 买入时佣金万分之2.5，卖出时佣金万分之2.5加千分之一印花税, 每笔交易佣金最低扣5块钱
    close_tax = 0.001
    buy_cost = 0.00025
    sell_cost = close_tax + buy_cost
    min_cost = 5


@dataclass
class Deal(DBModel):
    """
    当日成交
    """
    # 账户id
    balance_id: int
    # 成交单号
    deal_no: str
    # 委托单号
    entrust_no: str
    # 买卖类别
    bs_type: str
    # 委托数量
    entrust_amount: int
    # 成交数量
    deal_amount: int
    # 成交价格
    deal_price: float
    # 委托价格
    entrust_price: float
    # 成交时间,HHmmss
    deal_time: str
    # 股票代码
    stock_code: str
    # 股票名称
    stock_name: str

    def flush(self):
        db = DBHelper()
        query_sql = "select deal_no from deal where deal_no = '%s'" % self.deal_no
        if db.get_one(query_sql):
            return
        sql = "insert into deal (balance_id, deal_no, entrust_no, bs_type,entrust_amount, deal_amount,deal_price, entrust_price, " \
              "deal_time, stock_code, stock_name ) values ('%s','%s','%s','%s',%d,%d,'%s','%s','%s','%s','%s',)" % (
                  str(self.balance_id), self.deal_no, self.entrust_no, self.bs_type, self.entrust_amount,
                  self.deal_amount,
                  str(self.deal_price), str(self.entrust_price), self.deal_time, self.stock_code, self.stock_name
              )
        db.update(sql)
