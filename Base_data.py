import talib as tb
import tushare as ts
import pandas as pd
import akshare as ak

# def Get_stock_data(id,st,et):
#     stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=id, period="daily", start_date=st, end_date=et, adjust="")
#     df = pd.DataFrame(stock_zh_a_hist_df)
#     return df

def Get_stock_data(id,st,et):
    stock_zh_a_hist_df=ts.get_hist_data(id,start=st,end=et) #一次性获取全部日k线数据
    df = pd.DataFrame(stock_zh_a_hist_df)
    return df