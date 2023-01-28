import talib as tb

def use_KAMA(close,time):

    KAMA = tb.KAMA(close, timeperiod = time)
    return KAMA