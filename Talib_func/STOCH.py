import talib as tb
import pandas as pd

from Stock_helper.History_Data import His_Data
from Stock_helper.Now_data import Now_Data


def use_STOCH(high,low,close):
    k,d=tb.STOCH(high,low,close,
                fastk_period=9,
                slowk_period=5,
                slowk_matype=1,
                slowd_period=5,
                slowd_matype=1)  # 计算kdj的正确配置
    j=3.0*k-2.0*d
    return k,d,j

def use_STOCH_pro(ip_port,id,tf=0):
    global se_low, se_high, se_close
    h_d=His_Data(ip_port, id)
    df = h_d.get()
    se_close = df['今收']
    se_high = df['最高']
    se_low = df['最低']
    if tf==1:
        now_data = Now_Data(id)
        df = now_data.get()
        p_now = df['现价'].pop()
        p_low = df['最低'].pop()
        p_high = df['最高'].pop()

        se_close=df['今收']
        se_high=df['最高']
        se_low=df['最低']
        se_close[se_close.values.size] = str(p_now)
        se_high[se_high.values.size]=str(p_high)
        se_low[se_low.values.size]=str(p_low)
    k,d,j=use_STOCH(se_high, se_low,se_close)
    return k,d,j
