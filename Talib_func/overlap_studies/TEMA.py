import talib as tb
#TEMA：三重指数移动平均线
def use_TEMA(close, timeperiod = 30):
    TEMA = tb.TEMA(close, timeperiod=30)
    return TEMA
