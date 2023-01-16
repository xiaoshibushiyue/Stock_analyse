import talib as tb
import pandas as pd
import akshare as ak
from Base_data import Get_stock_data
#Chaikin A/D Oscillator
#是在AD指标的基础上计算长短周期的AD差，用于进一步观察市场中资金流动状况
#大于0买入（90天移动平均线之上才有效），小于0卖出（90天移动平均线之下才有效）
def use_ADOSC(id,st,et):
    df = Get_stock_data(id, st, et)
    a = tb.ADOSC(df["最高"], df["最低"], df["收盘"], df["成交量"],3,10)
    return a