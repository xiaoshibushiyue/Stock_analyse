import talib
def use_SAR(high,low):
    a=talib.SAR(high,low,2,2)
    return a