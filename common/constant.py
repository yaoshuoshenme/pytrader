import os
import time

class Constant:
    if "XDG_CONFIG_HOME" in os.environ:
        conf_dir = os.path.join(os.environ["XDG_CONFIG_HOME"], "s-trader")
    else:
        conf_dir = os.path.join(os.path.expanduser("~"), ".s-strader")
    config_path = os.path.join(conf_dir, "config.json")
    
    if "XDG_DATA_HOME" in os.environ:
        dataDir = os.path.join(os.environ["XDG_DATA_HOME"], "s-trader")
        if not os.path.exists(dataDir):
            os.mkdir(dataDir)
        cookie_path = os.path.join(dataDir, "cookie.txt")
        log_path = os.path.join(dataDir, "trader.log")
        storage_path = os.path.join(dataDir, "database.json")
    else:
        cookie_path = os.path.join(conf_dir, "cookie.txt")
        log_path = os.path.join(conf_dir, "trader.log")
        storage_path = os.path.join(conf_dir, "database.json")



print(int(round(time.time()*1000)))
