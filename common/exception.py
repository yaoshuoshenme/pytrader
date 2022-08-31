

class StockCommonException(Exception):
    def __init__(self, msg):
        self.message = msg
        self.code = -1