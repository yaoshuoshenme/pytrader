import easyquotation

import easyquant
from easyquant import  DefaultLogHandler, PushBaseEngine
from easyquant.log_handler.default_handler import MockLogHandler
from strategies.my_strategies import Strategy

print('backtest 回测 测试 ')

broker = 'mock'
need_data = 'account.json'

#
mock_start_dt = "20210101"
mock_end_dt= "20211111"


m = easyquant.MainEngine(broker, need_data,
                         quotation='local',
                         # quotation='jqdata',
                         bar_type="1d")

log_handler = MockLogHandler(context=m.context)

# 选择策略
strategy = Strategy(user=m.user, log_handler=log_handler, main_engine=m)

m.start_mock(mock_start_dt, mock_end_dt, strategy)

print('mock end')

print(m.user.get_balance())

for deal in m.user.get_current_deal():
    print(deal.deal_time, deal.bs_type, deal.deal_price, deal.deal_amount)
