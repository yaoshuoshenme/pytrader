import pandas as pd
from pandas import DataFrame
from easyquant.quotation.quotation import Quotation
from easytrader.utils.misc import file2dict
from persistence.mysql.db_config import DBHelper
from easyquant.quotation.quotation_util import to_tushare_code


"""本地行情
"""
class LocalQuotation(Quotation):

    def __init__(self):
        self.db_helper = DBHelper()


    """
    本地行情: 从数据库中读取
    """
    def get_bars(self, security, count, unit='1d',
                 fields=['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'vol'],
                 include_now=True, end_dt=None) -> DataFrame:
        
        # 把end_dt转换为YYYYMMDD
        end_dt = end_dt.strftime("%Y%m%d")

        # 如果security为None, 则返回当天所有股票的行情
        if security is None:
            # 从数据库中读取数据
            sql = f"SELECT {', '.join(fields)} FROM stock_daily WHERE trade_date = '{end_dt}'"
            df = self.db_helper.get_all(sql, return_type='df')
            return df
        else:
            stock_code = to_tushare_code(security)
            # 从数据库中读取数据
            sql = f"SELECT {', '.join(fields)} FROM stock_daily WHERE trade_date = '{end_dt}' AND ts_code = '{stock_code}'"
            df = self.db_helper.get_all(sql, return_type='df')
            return df

# print(LocalQuotation().get_all_trade_days()['cal_date'].head(1))
# print()