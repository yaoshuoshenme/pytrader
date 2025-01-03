from pandas import DataFrame

from .quotation import Quotation  # 使用相对导入
from . import quotation_util as utils

class FreeOnlineQuotation(Quotation):
    """
    实时行情
    """""

    def get_stock_type(self, stock_code: str):
        return "sh" if utils.is_shanghai(stock_code) else "sz"

    def _format_code(self, code: str) -> str:
        return "%s%s" % (self.get_stock_type(code), code)

    def get_bars(self, security, count, unit='1d',
                 fields=['date', 'open', 'high', 'low', 'close', 'volume'],
                 include_now=False, end_dt=None) -> DataFrame:
        # df = get_price(self._format_code(security), end_date=end_dt, count=security, frequency=unit)
        # return df
        pass