import talib as tb

#talib的macd函数返回三个值，第一个macd值，对应于DIF，第二个值macd_signal，对应于dea，第三个值macd_hist对应于macd。
#DIF 上穿DEA为买入 反之 （就是有一个势，看上穿或者下穿的力度）
#需要配合DMA TRIX使用
def use_MACD(close):
    macd,macdsignal,macdhist=tb.MACD(close)

    return macd,macdsignal,macdhist