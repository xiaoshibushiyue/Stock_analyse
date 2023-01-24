import talib as tb
# 均势指标
#显示了当前趋势的强度和方向
#正负 大小
from Base_data import Get_stock_data
def use_BOP(id, st, et):
    df = Get_stock_data(id, st, et)
    a = tb.BOP(df["开盘"],df["最高"], df["最低"],df["收盘"])
    return a