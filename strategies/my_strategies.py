#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Dict

from pandas import DataFrame

from easyquant import StrategyTemplate
from easyquant.context import Context


class Strategy(StrategyTemplate):
    name = "流动性溢价策略"

    watch_stocks = ['000776']

    def init(self):
        # for stock_code in self.watch_stocks:
        #     self.quotation_engine.watch(stock_code)
        pass

    def on_bar(self, context: Context, data: Dict[str, DataFrame]):
        print("on_bar事件")

    def on_open(self, context: Context):
        print("on_open事件")

    def on_close(self, context: Context):
        print("on_close事件")



    def pre_day_quotation(self):
        pass