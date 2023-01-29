from Strategy.Stock_bucket import insert_kdj, insert_kdj_g, insert_boll, insert_sar, insert_trix, insert_wr, insert_roc, \
    insert_brar, insert_macd
from Talib_func.BRAR import use_BRAR
from Talib_func.MACD import use_MACD
from Talib_func.ROC import use_ROC
from Talib_func.STOCH import use_STOCH
from Talib_func.TRIX import use_TRIX
from Talib_func.WR import use_WR
from Talib_func.overlap_studies.BBANDS import use_BBANDS
from Talib_func.overlap_studies.SAR import use_SAR


#只选可以买的 其他的不考虑
class Strategy:
    @staticmethod
    def KDJ(id,df):
        k, d, j = use_STOCH(df['high'],df['low'],df['close'])
        #买入参考
        if k.values[k.size - 1] < 20 and d.values[d.size - 1] < 20:
            insert_kdj(id)
        #卖出参考
        if k>80 and d>80:
            #提示注意
            pass
        #金叉
        if j<=k and j<=d:
            #这位置涉及到一个一个交叉的曲率
            if abs(k-d)<2 and abs(k-j)<2 and abs(j-d)<2:
                insert_kdj_g(id)
    @staticmethod
    def BOLL(id ,df):
        up,mid,low=use_BBANDS(df['close'])
        low = low.values[low.size - 1]
        mid = mid.values[mid.size - 1]
        high = up.values[up.size - 1]

        p = df.values[-1]
        p_low = p[int(4 + 1)]
        p_high = p[int(2 + 1)]
        p_now = p[int(3 + 1)]
        if float(p_low) <= low or float(p_high)>high:
            insert_boll(id)


    @staticmethod
    def SAR(id ,df):
        p = df.values[-1]
        p_now = p[int(3 + 1)]
        p_high = p[int(2 + 1)]
        a=use_SAR(df['high'],df['low'])
        a = a.values[a.size - 1]
        if float(p_high)>a:
            insert_sar(id)

    @staticmethod
    def TRIX(id ,df):
        a,ma=use_TRIX(df['close'], timeperiod=20)
        now = a.values[a.size - 1]
        if abs(float(now)-ma)/ma<0.05:
            insert_trix(id)
    @staticmethod
    def WR(id,df):
        wr=use_WR(df['high'],df['low'],df['close'])
        now = wr.values[wr.size - 1]
        if now>=90:
            insert_wr(id)

    @staticmethod
    def ROC(id,df):
        roc,ma=use_ROC(df['close'])
        now = roc.values[roc.size - 1]
        if now>6.5:
            if now>=ma:
                insert_roc(id)

    @staticmethod
    def BRAR(id,df):
        ar,br=use_BRAR(df['open'],df['high'],df['low'],df['close'])
        now_ar = ar.values[ar.size - 1]
        now_br = br.values[br.size - 1]
        if now_br<=40 or now_ar<40:
            insert_brar(id)
    @staticmethod
    def MACD(id,df):
        DIF,dea,macd=use_MACD(df['close'])
        dif = DIF.values[DIF.size - 1]
        m = macd.values[macd.size - 1]
        da=dea.values[dea.size - 1]
        macd
        if abs(dif-da)/dif<0.05 and m>-0.15:
            insert_macd(id)





