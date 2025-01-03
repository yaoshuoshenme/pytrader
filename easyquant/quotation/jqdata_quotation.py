from pandas import DataFrame
from .quotation import Quotation
from easytrader.utils.misc import file2dict
import jqdatasdk
import datetime
from  . import quotation_util as utils


class JQDataQuotation(Quotation):
    """
    JQData行情
    """""
    cache = {}

    def __init__(self):
        config = file2dict('jqdata.json')
        jqdatasdk.auth(config["user"], config["password"])

    def _get_cache_key(self, security, end_dt, unit):
        return "%s_%s_%s" % (self._format_code(security), utils.to_date_str(end_dt), unit)

    def get_stock_type(self, stock_code: str):
        return ".XSHG" if utils.is_shanghai(stock_code) else ".XSHE"

    def _format_code(self, code: str) -> str:
        return "%s%s" % (code, self.get_stock_type(code))

    def get_bars(self, security, count, unit='1d',
                 fields=['date', 'open', 'high', 'low', 'close', 'volume'],
                 include_now=True, end_dt=None) -> DataFrame:

        query_dt = end_dt
        if not isinstance(query_dt, datetime.datetime):
            query_dt = datetime.datetime.strptime(query_dt, "%Y-%m-%d")

        query_dt += datetime.timedelta(days=1)

        cache_key = self._get_cache_key(security, query_dt, unit)

        if cache_key in self.cache:
            df = self.cache[cache_key]
            return df[df.index <= end_dt] if "m" in unit else df

        cache_file = "data/jqdata-%s.csv" % cache_key

        if os.path.exists(cache_file):
            df = pd.read_csv(cache_file)
            df.index = df.date
            self.cache[cache_key] = df
            return df[df.index <= end_dt] if "m" in unit else df

        df = jqdatasdk.get_bars(self._format_code(security), count,
                                unit=unit,
                                fields=fields,
                                include_now=include_now,
                                # 取整天的数据
                                end_dt=to_date_str(query_dt), fq_ref_date=datetime.datetime.now())
        df.index = df.date
        df.sort_index(inplace=True)
        # 放入缓存
        self.cache[cache_key] = df

        df.to_csv(cache_file)

        # 过滤数据
        return df[df.index <= end_dt] if "m" in unit else df

