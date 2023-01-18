import talib as tb
import pandas as pd
#当布林线的上、中、下轨线同时向上运行时，表明股价强势特征非常明显，股价短期内将继续上涨，投资者应坚决持股待涨或逢低买入。
# 当布林线的上、中、下轨线同时向下运行时，表明股价的弱势特征非常明显，股价短期内将继续下跌，投资者应坚决持币观望或逢高卖出。
# 当布林线的上轨线向下运行，而中轨线和下轨线却还在向上运行时，表明股价处于整理态势之中。如果股价是处于长期上升趋势时，则表明股价是上涨途中的强势整理，投资者可以持股观望或逢低短线买入；如果股价是处于长期下跌趋势时，则表明股价是下跌途中的弱势整理，投资者应以持股观望或逢高减仓为主。
# 布林线的上轨线向上运行，而中轨线和下轨线同时向下运行，表明股价将经历一轮下跌，下跌的幅度将由开口的大小决定，反之，布林线的下轨线向下运行，而中轨线和上轨线同时向上运行，表明股价将经历一轮上涨，上涨的幅度将由开口的大小决定。
#（1）close：收盘价。

# （2）timeperiod：计算的周期，通常选择20天。
#
# （3） nbdevup：上限价格相对于周期内标准偏差的倍数，取值越大，则上限越大，通道越宽。
#
# （4）nbdevdn：下限价格相对于周期内标准偏差的倍数，取值越大，则下限越大，通道越宽。
#
# （5）matype：平均值计算类型，0代表简单一定平均，还可以有加权平均等方式。

from Base_data import Get_stock_data
from Stock_helper.his_data import his_dt
from Stock_helper.stock_now import stock_now_p


def use_BBANDS(id, st, et,tf):
    df = Get_stock_data(id, st, et)
    close=df["close"].values[0]
    df=df.iloc[::-1]
    if tf==1:
        sp=stock_now_p(id)
        df.loc[len(df.index)] = [20, 7, sp,3,3,3,3,1,1,1,1,1,1,1]
    upperband, middleband, lowerband= tb.BBANDS(df["close"],20,2,2)

    return upperband, middleband, lowerband,sp

def use_BBANDS_pro(ip_port,id,tf=0):
    sp=0
    pri_low=0
    se_close ,se_high,se_low= his_dt(ip_port,id,tf)
    sp=se_close.iloc[-1]
    if tf == 1:
        p_now,p_low,p_high=stock_now_p(id);
        sp=p_now
        pri_low=p_low
        se_close[se_close.values.size]=str(p_now)

    upperband, middleband, lowerband = tb.BBANDS(se_close, 20, 2, 2)


    return upperband, middleband, lowerband,sp,pri_low