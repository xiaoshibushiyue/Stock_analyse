import talib

def use_BRAR(open,high,low,close):
    HO = high -open
    OL = open - low
    HCY = high - close.shift(1)
    CYL = close.shift(1) - low
    # 计算AR、BR指标
    AR = talib.SUM(HO, timeperiod=26) / talib.SUM(OL, timeperiod=26) * 100
    BR = talib.SUM(HCY, timeperiod=26) / talib.SUM(CYL, timeperiod=26) * 100
    return  AR,BR
