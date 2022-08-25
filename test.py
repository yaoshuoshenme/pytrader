#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pytdx.hq import TdxHq_API
from pytdx.params import TDXParams

api = TdxHq_API()

with api.connect('119.147.212.81', 7709):
    # data = api.to_df(api.get_security_bars(9, 0, '000001', 0, 100)) #返回普通list
    # data = api.to_df(api.get_security_bars(0, 0, '000001', 4, 100))
    # data = api.to_df(api.get_minute_time_data(0, '000776'))
    # data = api.to_df(api.get_minute_time_data(1, '600389'))
    # data = api.to_df(api.get_transaction_data(TDXParams.MARKET_SH, '600389', 0, 100))
    # k线
    # data = api.to_df(api.get_minute_time_data(1, '600300'))
    data= api.get_and_parse_block_info('block_gn.dat')
    d = api.to_df(data)
    for row in d.itertuples():
        if getattr(row, 'code') == '000776':
            print(getattr(row, 'blockname'))
