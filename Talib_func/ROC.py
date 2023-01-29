import talib as tb

#一般行情在-6.50-6.5之间 注意均线的叉(与MAROC的叉) 价格和roc值同步升才好，价升roc不升要警惕
#MAROC=ROC的M日移动平均线
def use_ROC(close,time=12):
    ROC = tb.ROC(close, timeperiod=time)
    b=ROC[-6::]
    c=0
    for value in b:
        c=c+value
    MAROC=c/6.0
    
    return ROC,MAROC