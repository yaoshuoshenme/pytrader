import os

from pandas import DataFrame
import pandas as pd

from easytrader.utils.misc import file2dict

from .quotation import Quotation
import tushare as ts
from . import quotation_util as utils


class TushareQuotation(Quotation):
    """
    tushare 行情
    """""

    def __init__(self):
        tushare_config = file2dict('tushare.json')
        ts.set_token(tushare_config['token'])

    def get_stock_type(self, stock_code: str):
        return "SH" if utils.is_shanghai(stock_code) else "SZ"

    def _format_code(self, code: str) -> str:
        return "%s.%s" % (code, self.get_stock_type(code))

    def _get_cache_key(self, security, end_dt, unit):
        return "data/tushare_%s_%s_%s.csv" % (self._format_code(security), utils.to_date_str(end_dt), unit)

    def get_bars(self, security, count, unit='1d',
                 fields=['trade_date', 'open', 'high', 'low', 'close'],
                 include_now=False, end_dt=None) -> DataFrame:

        if unit == "1d":
            unit = "D"

        cache_file = self._get_cache_key(security, end_dt, unit)

        if os.path.exists(cache_file):
            df = pd.read_csv(cache_file)
            df.index = pd.to_datetime(df["trade_date"])
            return df

        df = ts.pro_bar(ts_code=self._format_code(security),
                        end_date=utils.to_date_str(end_dt),
                        freq=unit , # 只免费
                        asset='E',
                        limit=count)
        df.index = pd.to_datetime(df["trade_date"])
        df.sort_index(inplace=True)

        df.to_csv(cache_file)

        return df
