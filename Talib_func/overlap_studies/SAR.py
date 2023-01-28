import talib as tb
#抛物线指标
def use_SAR(high, low,acceleration, maximum):
    a=tb.SAR(high, low,acceleration,maximum)
    return a