import talib as tb

def use_ROC(close,time):
    ROC = tb.ROC(close, timeperiod=time)
    return ROC