from Talib_func.STOCH import use_STOCH


class strategy:
    #这位置的参数不好传啊---太多了
    @staticmethod
    def KDJ(k_,d_,j_,df):
        k, d, j = use_STOCH(df['最高'],df['最低'],df['今收'])
        if k.values[k.size - 1] < k_ and d.values[d.size - 1] < d_:
            return True
        return False
