import talib as tb
import pandas as pd
import akshare as ak

#平均趋向指标(趋势的强弱，而非趋势)
#ADX无法告诉你趋势的发展方向。可是，如果趋势存在，ADX可以衡量趋势的强度。不论上升趋势或下降趋势，
# ADX看起来都一样。ADX的读数越大，趋势越明显。衡量趋势强度时，需要比较几天的ADX 读数，
# 观察ADX究竟是上升或下降。ADX读数上升，代表趋势转强；如果ADX读数下降，意味着趋势转弱

#0-25	Absent or Weak Trend
#25-50	Strong Trend
#50-75	Very Strong Trend
#75-100	Extremely Strong Trend
from Base_data import Get_stock_data
def use_ADX(id, st, et):
    df = Get_stock_data(id, st, et)
    a = tb.ADX(df["最高"], df["最低"], df["收盘"],5)
    if (a>0 and a<25):
        print("弱趋势")
    if (a>25 and a<50):
        print("强趋势")
    if (a>50 and a<75):
        print("较强趋势")
    if (a>75 and a<100):
        print("非常强趋势")
    return a


