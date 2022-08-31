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
