import pandas as pd
from pandas import DataFrame
from .quotation import Quotation
from easytrader.utils.misc import file2dict
from persistence.mysql.db_config import DBHelper



"""本地行情
"""
class LocalQuotation(Quotation):

    def __init__(self):
        self.db_helper = DBHelper()


    """
    本地行情: 从数据库中读取
    """
    def get_bars(self, security, count, unit='1d',
                 fields=['date', 'open', 'high', 'low', 'close', 'volume'],
                 include_now=True, end_dt=None) -> DataFrame:
        # 从数据库中读取数据
        sql = f"SELECT {', '.join(fields)} FROM stock_bars WHERE security = '{security}' AND unit = '{unit}' ORDER BY date DESC LIMIT {count}"
        df = pd.read_sql(sql, self.conn)
        return df

# print(LocalQuotation().get_all_trade_days()['cal_date'].head(1))
# print()