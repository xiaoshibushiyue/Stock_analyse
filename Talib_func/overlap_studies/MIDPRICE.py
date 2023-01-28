import talib as tb

def use_MIDPRICE(close, time):
    MIDPOINT = tb.MIDPOINT(close, time)
    return MIDPOINT
