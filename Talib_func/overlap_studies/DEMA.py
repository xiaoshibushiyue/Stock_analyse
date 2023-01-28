import talib as tb
#双指数平均线大幅度的改善了传统平均线的延迟效应，可以较早的显示出价格反转的可能性，这个指标不仅只是当投资人在使用葛兰碧移动平均线八大法则时，
# 能够更快的获知价格突破或跌破的反转点，同时，将这个双指数用在MACD理论时，可用以替代传统的单指数EMA线上，而获得更早的买卖进出时点的讯号。


def use_DEMA(close,time):
    DEMA = tb.DEMA(close, timeperiod=time)
    return DEMA
