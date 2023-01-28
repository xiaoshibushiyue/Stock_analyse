import talib as tb

#均线 time 天数 就是软件上的均线
def use_SMA(close,time):
    SMA=tb.SMA(close,time)
    return SMA