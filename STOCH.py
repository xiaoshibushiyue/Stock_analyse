import talib as tb

def use_STOCH(high,low,close):
    k,d=tb.STOCH(high,low,close,
                fastk_period=9,
                slowk_period=5,
                slowk_matype=1,
                slowd_period=5,
                slowd_matype=1)  # 计算kdj的正确配置

