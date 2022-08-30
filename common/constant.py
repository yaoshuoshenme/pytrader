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
    east_money_keymap = {
        'c': '股票代码',
    }
