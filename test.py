from Base_data import Get_stock_data
from Talib_func.BRAR import use_BRAR
from Talib_func.MACD import use_MACD
from Talib_func.ROC import use_ROC
from Talib_func.SAR import use_SAR
from Talib_func.STOCHF import use_STOCHF
from Talib_func.TRIX import use_TRIX
from Talib_func.overlap_studies.BBANDS import use_BBANDS
from Talib_func.overlap_studies.DEMA import use_DEMA
from Talib_func.overlap_studies.KAMA import use_KAMA
from Talib_func.overlap_studies.SMA import use_SMA
from Talib_func.overlap_studies.T3 import use_T3





a=Get_stock_data('000519','2020-11-23','2023-01-20')
close=a['close'].reindex(a['close'].index[::-1])
high=a['high'].reindex(a['high'].index[::-1])
low=a['low'].reindex(a['low'].index[::-1])
open=a['open'].reindex(a['open'].index[::-1])

#a,b,c=use_MACD(close)
#ar,br=use_BRAR(open,high,low,close)
#a=use_DEMA(close,20)
#a.c=use_ROC(close,12)
a=use_SAR(high,low)
a,d=use_TRIX(close,12)
