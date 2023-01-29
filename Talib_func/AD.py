import talib as tb
import pandas as pd
import akshare as ak
from Base_data import Get_stock_data
#Chaikin A/D线
#长期趋势
#大于0买入（90天移动平均线之上才有效），小于0卖出（90天移动平均线之下才有效）



def use_AD(high,low,close,vol):
    #df=Get_stock_data(id,st,et)
    tb.LINEARREG_ANGLE()
    a = tb.AD(high, low, close, vol)
    return a


