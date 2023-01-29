import talib
def use_SAR(high,low):
    a=talib.SAR(high,low)
    return a