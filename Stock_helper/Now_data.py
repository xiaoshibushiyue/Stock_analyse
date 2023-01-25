import json
import pandas as pd
import requests


class Now_Data:
    def __init__(self,id):
        self.id=id

    def get(self):
        return self.__get_now()
    def __get_now(self):
        url = ""
        if self.id[0] == '6':
            self.id = 'sh' + self.id
            url = "https://hq.finance.ifeng.com/q.php?l=" + self.id
        else:
            self.id = 'sz' + self.id
            url = "https://hq.finance.ifeng.com/q.php?l=" + self.id
        r = requests.get(url)
        if r.status_code != 200:
            print('实时价格异常！')

        s = r.content.decode().strip('\n').strip('var json_q=').replace(';', '')
        text = json.loads(s)
        # 现价
        pri_now = text[self.id][0]
        # 昨收
        pri_yesterday_end = text[self.id][1]
        # 价差（今天-昨天）
        pri_Dvalue = text[self.id][2]
        # 涨幅
        pri_Increase = text[self.id][3]
        # 今开
        pri_today_start = text[self.id][4]
        # 最高
        pri_high = text[self.id][5]
        # 最低
        pri_low = text[self.id][6]
        # 今收
        pri_today_now = text[self.id][7]
        # 总成交量(手)
        Turnover_s = text[self.id][9]
        # 总成交额（元）
        Turnover_y = text[self.id][10]
        df = pd.DataFrame([{'现价':pri_now, '昨收':pri_yesterday_end, '价差':pri_Dvalue, '涨幅': pri_Increase,'今开':pri_today_start, '最高': pri_high, '最低': pri_low, '今收': pri_today_now, '总手':Turnover_s, '成交额':Turnover_y}])

        return df
