import talib as tb
#EMA（Exponential Moving Average）是指数移动平均值。也叫 EXPMA 指标，它也是一种趋向类指标，指数移动平均值是以指数式递减加权的移动平均。
#EMA指标由于其计算公式中着重考虑了当天价格（当期）行情的权重，决定了其作为一类趋势分析指标，在使用中克服了MACD指标对于价格走势的滞后性缺陷，同时，
# 也在一定程度上消除了DMA指标在某些时候对于价格走势所产生的信号提前性，是一个非常有效的分析指标。
def use_EMA(close,time):
    EMA = tb.EMA(close, timeperiod=time)
    return EMA