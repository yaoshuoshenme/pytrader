from api.eastmoney_api import EastMoneyApi
from api.tushare_api import TushareApi
from config.local_data_repo import LocalDataRepo
import json
import os

easy_api = EastMoneyApi()
# data = easy_api.get_limit_up_pool('20220830')
# print(json.dumps(data))

# tsApi = TushareApi()
# data = tsApi.get_trade_days()
# LocalDataRepo.write_data(data, 'trade_days.xlsx', 'pd')
# print(data)


# data = LocalDataRepo.read_json_2_df('block_code.json')
# print(data)
data = easy_api.get_block_rank()
print(data)


