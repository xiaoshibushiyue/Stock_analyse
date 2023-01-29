import talib

#相比kdj更敏感
def use_STOCHF(high,low,close,fastk_period=5,fastd_period=3):
    fastk, fastd = talib.STOCHF(high, low, close, fastk_period, fastd_period)
    j = 3.0 * fastk - 2.0 * fastd
    return fastk, fastd ,j