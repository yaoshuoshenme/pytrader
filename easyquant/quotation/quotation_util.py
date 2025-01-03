import datetime



def is_shanghai(stock_code):
    """判断股票ID对应的证券市场
    匹配规则
    ['50', '51', '60', '90', '110'] 为 sh
    ['00', '13', '18', '15', '16', '18', '20', '30', '39', '115'] 为 sz
    ['5', '6', '9'] 开头的为 sh， 其余为 sz
    :param stock_code:股票ID, 若以 'sz', 'sh' 开头直接返回对应类型，否则使用内置规则判断
    :return 'sh' or 'sz'"""
    assert type(stock_code) is str, "stock code need str type"
    sh_head = ("50", "51", "60", "90", "110", "113",
               "132", "204", "5", "6", "9", "7")
    return stock_code.startswith(sh_head)

def to_date_str(dt):
    if dt is None:
        return None
    if isinstance(dt, datetime.date) or isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d")
    

def use_quotation(source: str):
    from easyquant.quotation.jqdata_quotation import JQDataQuotation
    from easyquant.quotation.tushare_quotation import TushareQuotation
    from easyquant.quotation.local_quotation import LocalQuotation
    from easyquant.quotation.free_online_qotation import FreeOnlineQuotation

    """
    对外API，行情工厂
    :param source:
    :return:
    """
    if source in ["jqdata"]:
        return JQDataQuotation()
    if source in ["tushare"]:
        return TushareQuotation()
    if source in ["local"]:
        return LocalQuotation()
    return FreeOnlineQuotation()
