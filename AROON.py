import talib as tb
#返回值up和down
#当Aroon-Up高于50并接近100且Aroon-Down低于50时，这很好地表明了上升趋势。同样，当Aroon-Down高于50并接近100，而Aroon-Up低于50时，可能会出现下降趋势。
from Base_data import Get_stock_data
def use_AROON(id, st, et):
    df = Get_stock_data(id, st, et)
    a = tb.AROON(df["最高"], df["最低"],3)
    return a