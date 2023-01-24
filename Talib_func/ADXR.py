import talib as tb
import pandas as pd
import akshare as ak

#A rising ADXR, with DI+ above the D- indicates a strengthening bullish market.
#A rising ADXR, with DI- above DI+ indicates a strengthening bearish market
from Base_data import Get_stock_data
def use_ADXR(id, st, et):
    df = Get_stock_data(id, st, et)
    a = tb.ADXR(df["最高"], df["最低"], df["收盘"],5)
    if (a>0 and a<25):
        print("不可参考")
    if (a>25):
        print("可参考趋势")
    return a


