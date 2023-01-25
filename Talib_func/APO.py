import talib as tb
import pandas as pd
import akshare as ak

#绝对价格振荡器 (APO) 基于两条不同长度的移动平均线之间的绝对差异，一条“快速”移动平均线和一条“慢速”移动平均线
#当APO上穿0，表示买入信号；

# 当APO下穿0，表示卖出信号。
from Base_data import Get_stock_data
def use_APO(close):
    #df = Get_stock_data(id, st, et)

    a = tb.APO(close,3,5)
    if (a>0):
        print("买入")
    if (a<0):
        print("卖出")
    return a


