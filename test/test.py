#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from pytdx.hq import TdxHq_API
from pytdx.params import TDXParams

api = TdxHq_API()

with api.connect('tdx.xmzq.com.cn', 7709):
    # data = api.to_df(api.get_security_bars(9, 0, '000001', 0, 100)) #返回普通list
    # data = api.to_df(api.get_security_bars(0, 0, '000001', 4, 100))
    # data = api.to_df(api.get_minute_time_data(0, '000776'))
    # data = api.to_df(api.get_minute_time_data(1, '600389'))
    # data = api.to_df(api.get_transaction_data(TDXParams.MARKET_SH, '600389', 0, 100))
    # k线
    # data = api.to_df(api.get_minute_time_data(1, '600300'))

    # 获取股票即时行情
    # data = api.get_security_quotes([(1, '518880')])
    # print(data)

    # 获取历史分钟数据
    # data = api.get_history_minute_time_data(1, '518880', 20240827)
    # print(api.to_df(data))

    # 查询分笔成交
    # data = api.get_transaction_data(1, '518880', 0, 30)
    # print(api.to_df(data))

    #     查询历史分笔成交
    # data = api.get_history_transaction_data(1, '518880', 0, 10, 20240827)
    # print(api.to_df(data))

    # 查询公司信息目录
    # data = api.get_company_info_category(TDXParams.MARKET_SZ, '000001')
    # print(api.to_df(data))

    # 读取公司信息详情
    # data = api.get_company_info_content(0, '000001', '000001.txt', 232258, 7301)
    # print(data)

    # 读取财务信息
    # data = api.get_finance_info(0, '000001')
    # print(data)


    # 获取k线
    # data = api.get_security_bars(9, 0, '000001', 0, 10)
    # print(api.to_df(data))


    # 批量获取股票行情
    data = api.get_security_quotes([(0, '000001'), (1, '600300')])
    print(data)
