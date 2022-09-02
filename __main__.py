import os


import logging
from common.simplelog import SimpleLog
from threading import Event



# easy_api = EastMoneyApi()
# data = easy_api.get_limit_up_pool('20220830')
# print(json.dumps(data))

# tsApi = TushareApi()
# data = tsApi.get_trade_days()
# LocalDataRepo.write_data(data, 'trade_days.xlsx', 'pd')
# print(data)


# data = LocalDataRepo.read_json_2_df('block_code.json')
# print(data)
# data = easy_api.get_block_rank()
# print(data)

log = SimpleLog.get(__file__)
log.info("运行成功")

Event().wait()