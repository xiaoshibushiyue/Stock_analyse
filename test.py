from Base_data import Get_stock_data
from Talib_func.ROC import use_ROC
from Talib_func.overlap_studies.BBANDS import use_BBANDS
from Talib_func.overlap_studies.DEMA import use_DEMA
from Talib_func.overlap_studies.KAMA import use_KAMA
from Talib_func.overlap_studies.SMA import use_SMA
from Talib_func.overlap_studies.T3 import use_T3

a=Get_stock_data('000519','2020-11-23','2023-01-20')
d=a['close'].reindex(a['close'].index[::-1])
s=use_ROC(d,5)