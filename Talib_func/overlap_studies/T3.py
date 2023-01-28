import talib as tb

#三重移动平均线
def use_T3(close,timeperiod=5,vfactor=0):
    T3 =tb.T3(close, timeperiod=5, vfactor=0)
    return T3

