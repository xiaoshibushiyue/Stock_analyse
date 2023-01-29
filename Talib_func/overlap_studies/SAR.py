import talib as tb
#抛物线指标
def use_SAR(high, low,):
    a=tb.SAR(high, low)
    return a