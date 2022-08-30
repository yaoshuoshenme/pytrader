from api.eastmoney_api import EastMoneyApi


easy_api = EastMoneyApi()
data = easy_api.get_limit_up_pool('20220830')
print(data)