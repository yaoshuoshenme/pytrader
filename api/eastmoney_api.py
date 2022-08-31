from logging import getLogger
import sys
import requests
from http.cookiejar import Cookie, CookieJar, MozillaCookieJar
from common.constant import Constant
import time
from http.client import HTTPConnection

log = getLogger(__name__)

DEFAULT_TIMEOUT = 10
BASE_URL = "http://push2ex.eastmoney.com"


class EastMoneyApi(object):

    def __init__(self) -> None:
        self.header = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Referer": "http://quote.eastmoney.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }
        cookie_jar = MozillaCookieJar(Constant.cookie_path)
        # cookie_jar.load()
        self.session = requests.Session()
        self.session.cookies = cookie_jar
        for cookie in cookie_jar:
            if cookie.is_expired():
                cookie_jar.clear()
                break

    def request(self, method, path, params={}, default={"code": -1}, custom_cookies={}):
        endpoint = "{}{}".format(BASE_URL, path)
        data = default

        for k, v in custom_cookies.items():
            cookie = self._make_cookie(k, v)
            self.session.cookies.set_cookie(cookie)

        resp = None
        try:
            resp = self._raw_request(method, endpoint, params)
            data = resp.json()
        except requests.exceptions.RequestException as e:
            log.error(e)
        except ValueError:
            log.error("Path: {}, response: {}".format(path, resp.text[:200]))
        finally:
            return data

    def _raw_request(self, method, endpoint, data=None):
        resp = None
        if method == "GET":
            resp = self.session.get(endpoint, params=data, headers=self.header, timeout=DEFAULT_TIMEOUT)
        elif method == "POST":
            resp = self.session.post(endpoint, params=data, headers=self.header, timeout=DEFAULT_TIMEOUT)
        return resp

    @staticmethod
    def _make_cookie(k, v):
        return Cookie(
            version=0,
            name=k,
            value=v,
            port=None,
            port_specified=False,
            domain="quote.eastmoney.com",
            domain_specified=True,
            domain_initial_dot=False,
            path="/",
            path_specified=True,
            secure=False,
            expires=None,
            discard=False,
            comment=None,
            comment_url=None,
            rest={},
        )

    def get_stock_code(self):
        """获取股票代码,包括公司名称，上市时间等
        """
        pass

    def get_block_info(self):
        """获取板块信息
        """
        pass

    def get_stock_rank(self, reverse=False):
        """获取股票涨幅排行榜

        Args:
            reverse (bool, optional): 倒序. Defaults to False.
        """
        pass

    def get_limit_up_pool(self, date: str = None):
        """获取涨停池信息

        Args:
            date (_type_, optional): 时间. Defaults to None, 格式：20220830.
            start (_type_, optional): 开始时间. Defaults to None.
            end (_type_, optional): 结束时间. Defaults to None.
        """
        path = "/getTopicZTPool"
        params = dict(
            ut="7eea3edcaed734bea9cbfc24409ed989",
            dpt="wz.ztzt",
            Pageindex=0,
            pagesize=100,
            sort="fbt:asc",
            date=date,
            _=int(round(time.time() * 1000))
        )
        return self.request("GET", path, params)

    def get_limit_down_pool(self, date=None, start=None, end=None):
        """获取跌停池信息

        Args:
            date (_type_, optional): 时间. Defaults to None.
            start (_type_, optional): 开始. Defaults to None.
            end (_type_, optional): 结束. Defaults to None.
        """
        pass
