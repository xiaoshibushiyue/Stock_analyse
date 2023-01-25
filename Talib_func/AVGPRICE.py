import talib as tb
#平均价格函数
#主要用于计算开盘价、收盘价、最高价、最低价之间的均值
from Base_data import Get_stock_data
def use_AVGPRICE(open,high,low,close):
    #df = Get_stock_data(id, st, et)
    a = tb.AVGPRICE(open,high,low,close)
    return a