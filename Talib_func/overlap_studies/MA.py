import talib as tb
#移动平均线，Moving Average，简称MA，原本的意思是移动平均，由于我们将其制作成线形，
# 所以一般称之为移动平均线，简称均线。它是将某一段时间的收盘价之和除以该周期。 比如日线MA5指5天内的收盘价除以5。

def use_MA(close,time,):
    a=tb.MA(close, timeperiod = time, matype = 0)
    return a