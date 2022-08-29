import requests


base_url = ""


def get_stock_code():
    """获取股票代码,包括公司名称，上市时间等
    """
    pass

def get_block_info():
    """获取板块信息
    """
    pass

def get_stock_rank(reverse=False):
    """获取股票涨幅排行榜

    Args:
        reverse (bool, optional): 倒序. Defaults to False.
    """
    pass

def get_limit_up_pool(date=None, start=None, end=None):
    """获取涨停池信息

    Args:
        date (_type_, optional): 时间. Defaults to None.
        start (_type_, optional): 开始时间. Defaults to None.
        end (_type_, optional): 结束时间. Defaults to None.
    """
    pass

def get_limit_down_pool(date=None, start=None, end=None):
    """获取跌停池信息

    Args:
        date (_type_, optional): 时间. Defaults to None.
        start (_type_, optional): 开始. Defaults to None.
        end (_type_, optional): 结束. Defaults to None.
    """
    pass