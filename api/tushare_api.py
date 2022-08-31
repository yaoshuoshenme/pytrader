import tushare as ts
import os
import json

account_path = os.path.join(os.path.dirname(__file__), os.path.pardir, "account.json")


class TushareApi(object):
    def __init__(self) -> None:
        with open(account_path, mode='r', encoding='utf-8') as f:
            account_config = json.load(f)
        self.token = account_config['tushare']['token']
        self.api = ts.pro_api(self.token)

    def _login(self):
        """登陆"""
        pass

    def get_all_code(self):
        """获取所有code"""
        pass

    def get_trade_days(self, start_date='20220901', end_date='20320901'):
        """
        exchange	    str	Y	交易所 SSE上交所 SZSE深交所
        cal_date	    str	Y	日历日期
        is_open	        str	Y	是否交易 0休市 1交易
        pretrade_date	str	Y	上一个交易日
        """
        df = self.api.trade_cal(exchange='', start_date=start_date, end_date=end_date,
                           fields='exchange,cal_date,is_open,pretrade_date', is_open='1')
        return df

