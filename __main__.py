from api.eastmoney_api import EastMoneyApi
from api.tushare_api import TushareApi
from config.local_data_repo import LocalDataRepo
import json

# easy_api = EastMoneyApi()
# data = easy_api.get_limit_up_pool('20220830')
# print(json.dumps(data))

# tsApi = TushareApi()
# data = tsApi.get_trade_days()
# print(data)

data = LocalDataRepo.read_data('trade_days.json')
print(data)