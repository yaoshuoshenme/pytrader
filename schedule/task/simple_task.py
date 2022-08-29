

from abc import abstractmethod

class SimpleTask(object):
    """
    任务基础类
    """
    def __init__(self, trigger, *args, **trigger_args) -> None:
        self.trigger = trigger
        self.trigger_args = trigger_args
    
    @abstractmethod
    def run():
        """
        执行
        """
        pass
    
    def restart():
        """重启任务
        """
        pass
    
    
class StockBaseDataSyncTask(SimpleTask):
    
    def __init__(self, trigger, trigger_args:dict) -> None:
        super().__init__(trigger, seconds = trigger_args['seconds'])
 
    def run(self):
        print("trigger:{}, trigger_args:{}".format(self.trigger, self.trigger_args))
        print("执行股票基础数据同步")
    

    
