#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pandas import DataFrame
from pytdx.hq import TdxHq_API

from easyquant.quotation import Quotation

api = TdxHq_API()

class TdxQuotation(Quotation):
    def __init__(self):
        api.connect('119.147.212.81', 7709)

    def get_bars(self, security, count, unit='1d',
                 fields=['date', 'open', 'high', 'low', 'close', 'volume'],
                 include_now=False, end_dt=None) -> DataFrame:
        """
        获取历史数据(包含快照数据), 可查询单个标的多个数据字段
        """
        pass
