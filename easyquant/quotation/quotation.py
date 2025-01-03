import abc
import datetime

from pandas import DataFrame
from persistence.mysql.db_config import DBHelper


class Quotation(metaclass=abc.ABCMeta):
    """行情获取基类"""

    def get_bars(self, security, count, unit='1d',
                 fields=['date', 'open', 'high', 'low', 'close', 'volume'],
                 include_now=False, end_dt=None) -> DataFrame:
        """
        获取历史数据(包含快照数据), 可查询单个标的多个数据字段

        :param security 股票代码
        :param count 大于0的整数，表示获取bar的个数。如果行情数据的bar不足count个，返回的长度则小于count个数。
        :param unit bar的时间单位, 支持如下周期：'1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'。'1w' 表示一周，‘1M' 表示一月。
        :param fields 获取数据的字段， 支持如下值：'date', 'open', 'close', 'high', 'low', 'volume', 'money'
        :param include_now 取值True 或者False。 表示是否包含当前bar, 比如策略时间是9:33，unit参数为5m， 如果 include_now=True,则返回9:30-9:33这个分钟 bar。
        :param end_dt: 查询的截止时间
        :param fq_ref_date: 复权基准日期，为None时为不复权数据
        :param df: 默认为True，传入单个标的返回的是一个dataframe，传入多个标的返回的是一个multi-index dataframe
                当df=False的时候，当单个标的的时候，返回一个np.ndarray，多个标的返回一个字典，key是code，value是np.array；
        :return numpy.ndarray格式
        """
        pass

    def get_all_trade_days(self):
        """
        所有交易日期
        :return:
        """
        # trade_days = jqdatasdk.get_all_trade_days()
        # data = pd.Series(trade_days.tolist())
        # data = data.apply(lambda x: x.strftime("%Y-%m-%d"))
        # return data.values.tolist()
        # return get_all_trade_days()
        # 从数据库中获取
        from persistence.mysql.db_config import DBHelper
        sql = "select * from stock_trade_days"
        days = DBHelper().get_all(sql, return_type='df')
        return days

    def get_price(self, security: str, date):
        df = self.get_bars(security, 1, unit='1d', end_dt=date, fields=['close', 'date'])
        return df.close[0]

