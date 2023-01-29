import talib

#威廉指标--抄底不错 100为底部
def use_WR(high, low, close,time=14):
    a=talib.WILLR(high, low, close,time)
    return a