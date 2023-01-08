from abc import abstractmethod
from common.simplelog import SimpleLog

class SimpleTask(object):
    """
    任务基础类
    """

    def __init__(self, trigger, trigger_args: dict) -> None:
        self.trigger = trigger
        self.trigger_args = trigger_args

    @abstractmethod
    def run(self):
        """
        执行
        """
        pass

    def restart(self):
        """重启任务
        """
        pass


class StockBaseDataSyncTask(SimpleTask):

    def __init__(self, trigger, trigger_args: dict):
        self.log = SimpleLog.get(__name__)
        super().__init__(trigger, trigger_args)

    def run(self):
        self.log.info("trigger:{}, trigger_args:{}".format(self.trigger, self.trigger_args))
        print("执行股票基础数据同步")
