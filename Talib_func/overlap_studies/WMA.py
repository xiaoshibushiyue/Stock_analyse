import talib as tb
# 移动加权平均法
def use_WMA(close):
    WMA = tb.WMA(close, timeperiod=30)
    return WMA