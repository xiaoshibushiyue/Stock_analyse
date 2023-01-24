import talib as tb
#两只乌鸦
from Base_data import Get_stock_data
def use_CDL2CROWS(id, st, et):
    '''
    三日K线模式，第一天长阳，第二天高开收阴，第三天再次高开继续收阴。收盘比前一日收盘价低，预示股价下跌
    :param id:
    :param st:
    :param et:
    :return:0 表示不是
    '''
    df = Get_stock_data(id, st, et)
    a = tb.STOCH(df["开盘"],df["最高"], df["最低"],df["收盘"])
    return a