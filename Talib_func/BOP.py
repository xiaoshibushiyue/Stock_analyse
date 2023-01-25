import talib as tb
# 均势指标
#显示了当前趋势的强度和方向
#正负 大小
from Base_data import Get_stock_data
def use_BOP(open,high,low,close):
    #df = Get_stock_data(id, st, et)
    a = tb.BOP(open,high,low,close)
    return a