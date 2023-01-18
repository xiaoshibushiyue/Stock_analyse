import talib as tb
import pandas as pd

from Stock_helper.his_data import his_dt
from Stock_helper.stock_now import stock_now_p


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
    se_close, se_high, se_low = his_dt(ip_port, id, tf)
    if tf==1:
        p_now, p_low, p_high = stock_now_p(id);
        se_close[se_close.values.size] = str(p_now)
        se_high[se_high.values.size]=str(p_high)
        se_low[se_low.values.size]=str(p_low)
    k,d,j=use_STOCH( se_high, se_low,se_close)
    return k,d,j
