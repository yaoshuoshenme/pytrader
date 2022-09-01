#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import uuid
from typing import List

from easytrader import webtrader, exceptions
from persistence.mysql.db_config import DBHelper
from persistence.stock_db import Entrust, Position, Deal
from threading import Lock


class SimulateTrader(webtrader.WebTrader):
    config_path = os.path.dirname(__file__) + "/config/simulate.json"
    balance_account = {}
    balance_lock = {}
    position_dic = {}
    entrusts_dic = {}
    deal_dic = {}

    def __init__(self, **kwargs):
        super(SimulateTrader, self).__init__()
        self._load()
        self._generate_lock()

    def buy_spec(self, balance, security, price=0, amount=0, volume=0, entrust_prop=0):
        """买入卖出股票
        :param balance: 指定账户
        :param security: 股票代码
        :param price: 买入价格
        :param amount: 买入股数
        :param volume: 买入总金额 由 volume / price 取整， 若指定 price 则此参数无效
        :param entrust_prop:
        """
        return self._trade(balance, security, price, amount, volume, "B")

    def sell_spec(self, balance, security, price=0, amount=0, volume=0, entrust_prop=0):
        """卖出股票
        :param balance: 指定账户
        :param security: 股票代码
        :param price: 卖出价格
        :param amount: 卖出股数
        :param volume: 卖出总金额 由 volume / price 取整， 若指定 price 则此参数无效
        :param entrust_prop:
        """
        return self._trade(balance, security, price, amount, volume, "S")



    def _trade(self, balance, security, price=0, amount=0, volume=0, entrust_bs="B"):
        """
        调仓
        :param security:
        :param price:
        :param amount:
        :param volume:
        :param entrust_bs:
        :return:
        """
        with self.balance_lock[balance.id]:

            cost = self.calculate_cost(amount, price, entrust_bs)
            if not volume:
                volume = float(price) * amount # 可能要取整数

            total_cost = volume + cost
            if balance.current_balance < total_cost and entrust_bs == "B":
                raise exceptions.TradeError(u"没有足够的现金进行操作")
            if amount == 0:
                raise exceptions.TradeError(u"数量不能为0")

            entrust_no = str(uuid.uuid1())
            self._add_entrusts(balance.id, Entrust(
                balance_id=balance.id,
                entrust_no=entrust_no,
                bs_type=entrust_bs,
                entrust_status='已成交',
                report_time=self.time.strftime("%Y-%m-%d %H:%M:%S"),
                stock_code=security,
                stock_name=security,
                entrust_amount=amount,
                entrust_price=price,
                cost=cost
            ))

            self._add_deals(balance.id, Deal(
                balance_id=balance.id,
                deal_no=str(uuid.uuid1()),
                entrust_no=entrust_no,
                bs_type=entrust_bs,
                stock_code=security,
                stock_name=security,
                deal_amount=amount,
                deal_price=price,
                entrust_amount=amount,
                entrust_price=price,
                deal_time=self.time.strftime("%Y-%m-%d %H:%M:%S")
            ))


            position = self._find_hold_position(security, self.position_dic[balance.id])

            if entrust_bs == "B":
                # 更新持仓
                balance.enable_balance = balance.enable_balance - total_cost
                balance.current_balance = max (0, balance.current_balance - total_cost)
                balance.asset_balance -= total_cost
                if position:
                    position.cost_price = (position.current_amount * position.cost_price + volume) / (
                            position.current_amount + amount)
                    position.current_amount += amount
                else:
                    self.position_dic[balance.id].append(Position(
                        balance_id=balance.id,
                        current_amount=amount,
                        cost_price=total_cost / amount,
                        last_price=price,
                        market_value=volume,
                        stock_code=security,
                        stock_name=security,
                        enable_amount=amount,
                        income_balance=0
                    ))
            else:
                # 卖出
                if position:
                    position.current_amount -= amount
                    # 更新持仓
                    balance.enable_balance = balance.enable_balance + volume - cost
            self._flush_data(balance)



    def _load(self):
        # 账户信息
        self._load_balance()
        # 持仓信息
        self._load_position()
        # 委托信息
        self._load_entrusts()
        # 账单信息
        self._load_deals()

    def _load_balance(self):
        """
        加载账户信息
        """
        # 账户信息
        balance_data = DBHelper().get_all("select * from balance where 1=1")
        for b in balance_data:
            self.balance_account[b['id']] = b
            self.balance_lock[b['id']] = Lock()


    def _load_position(self):
        """
        加载持仓信息
        """
        position_data = DBHelper().get_all("select * from positions where 1=1")
        for d in position_data:
            if self.position_dic[d['balance_id']] == None:
                self.position_dic[d['balance_id']] = []
            self.position_dic[d['balance_id']].apend(d)
            
    def add_position(self, balance_id, position: Position):
        """
        增加持仓
        """
        self.position_dic[balance_id].append(position)

    def _load_entrusts(self):
        """
        加载委托信息
        """
        entrusts_data = DBHelper().get_all("select * from entrusts where 1=1")
        for d in entrusts_data:
            if self.entrusts_dic[d['balance_id']] == None:
                self.entrusts_dic[d['balance_id']] = []
            self.entrusts_dic[d['balance_id']].apend(d)
            
    def _add_entrusts(self, balance_id, entrust: Entrust):
        """
        添加委托信息
        """
        self.entrusts_dic[balance_id].append(entrust)

    def _load_deals(self):
        """
        加载账单信息
        """
        deal_data = DBHelper().get_all("select * from deals where 1=1")
        for d in deal_data:
            if self.deal_dic[d['balance_id']] == None:
                self.deal_dic[d['balance_id']] = []
            self.deal_dic[d['balance_id']].apend(d)
            
    def _add_deals(self, balance_id, deal: Deal):
        """
        添加账单信息
        """
        self.deal_dic[balance_id].append(deal)


    def _find_hold_position(self, code: str, positions:List[Position]) -> Position:
        for position in positions:
            if position.stock_code == code:
                return position
        return None

    def _generate_lock(self):
        for b_id in self.balance_account:
            self.balance_lock[b_id] = Lock()

    def _flush_data(self, balance):
        balance.flush()
        [p.flush() for p in self.position_dic.get(balance.id)]
        [e.flush() for e in self.entrusts_dic.get(balance.id)]
        [d.flush() for d in self.deal_dic.get(balance.id)]

    def shutdown(self):
        [self._flush_data(b) for b in self.balance_account.values()]