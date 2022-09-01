import os
from sys import platform
import time


class Constant:
    if platform == 'win32':
        conf_dir = "D:\\trader\\config"
    else:
        conf_dir = os.path.join(os.path.expanduser("~"), "trader")

    if not os.path.exists(conf_dir):
        os.makedirs(conf_dir)

    config_path = os.path.join(conf_dir, "config.json")
    cookie_path = os.path.join(conf_dir, "cookie.txt")
    log_path = os.path.join(conf_dir, "trader.log")
    storage_path = os.path.join(conf_dir, "database.json")

    # 东方财富指标映射
    eastmoney_zt_keymap = {
        'c': '股票代码',
        'n': '股票名称',
        'p': '价格 * 1000',
        'zdp': '涨跌幅',
        'amount': '成交额',
        'ltsz': '流通市值',
        'tshare': '总市值',
        'hs': '换手',
        'lbc': '连板数',
        'fbt': '首次封板时间',
        'lbt': '最后封板时间',
        'fund': '封板资金',
        'zbc': '炸板次数',
        'hybk': '行业板块',
        'zttj': '涨停统计',
        'days': '几天',
        'ct': '几板'
    }
    # 个股指标
    eastmoney_stock_keymap = {
        'f1': '',
        'f2': '最新价',
        'f3': '涨跌幅%',
        'f4': '涨跌额',
        'f5': '成交量（手）',
        'f6': '成交额（元）',
        'f7': '振幅 %',
        'f8': '换手率 %',
        'f9': '市盈率（动态）',
        'f10': '量比',
        'f11': '5分钟涨跌',
        'f12': '代码',
        'f13': '',
        'f14': '股票名称',
        'f15': '最高价',
        'f16': '最低价',
        'f17': '今开',
        'f18': '昨收',
        'f19': '',
        'f20': '总市值',
        'f21': '流通市值',
        'f22': '涨速',
        'f23': '市净率',
        'f24': '60日涨幅',
        'f25': '年初至今涨幅',

        # ------ 板块相关指标------
        'f43': '',
        'f44': '最高(*100)',
        'f45': '最低（*100）',
        'f46': '',
        'f47': '',
        'f48': '',
        'f49': '',
        'f50': '量比（*100）',
        'f57': '板块代码',
        'f58': '板块名称',
        'f59': '',
        'f60': '昨收（*100）',
        'f62': '',
        'f84': '',
        'f85': '',
        'f86': '',

        'f104': '上涨家数（板块）',
        'f105': '下跌家数（板块）',
        'f115': '市盈率',
    }



