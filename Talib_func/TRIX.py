
import talib


#TRIX指标是属于中长线技术指标，其最大的优点就是可以过滤短期波动的干扰，以避免频繁操作而带来的失误和损失。
# 因此TRIX指标最适合于对行情的中长期走势的研判。在股市软件上TRIX指标有两条线，一条线为TRIX线，另一条线为TRMA线。TRIX指标的一般研判标准主要集中在TRIX线和TRMA线的交叉情况的考察上。
#，有时还会出现频繁交叉的情况，通常还有一个时间上的确认
#a,d=use_TRIX(close,12)
def use_TRIX(close, timeperiod=20):
    TRIX=talib.TRIX(close, timeperiod)
    #MA取12
    b=TRIX[-20::]
    c=0
    for value in b:
        c=c+value

    TRMA=c/20.0
    return TRIX,TRMA

