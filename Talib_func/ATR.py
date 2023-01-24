import talib as tb
#真实波动幅度均值
#主要应用于了解股价的震荡幅度和节奏，在窄幅整理行情中用于寻找突破时机。通常情况下股价的波动幅度会保持在一定常态下，但是如果有主力资金进出时，股价波幅往往会加剧
#如果当前价格比之前的价格高一个ATR的涨幅，买入股票
# 如果之前的价格比当前价格高一个ATR的涨幅，卖出股票
from Base_data import Get_stock_data
def use_ATR(id, st, et):
    df = Get_stock_data(id, st, et)

    a = tb.ATR(df["最高"], df["最低"],df["收盘"],5)
    return a