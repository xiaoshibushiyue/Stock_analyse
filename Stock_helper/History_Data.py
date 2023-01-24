import threading
import requests
import json
import pandas as pd
class His_Data:
    def __init__(self,ip_port,id):
        self.ip_port=ip_port
        self.id=id
    def get(self):
        return self.__get_his_Data()
    def __get_his_Data(self):
        proxies = {"http": self.ip_port}
        if self.id[0] == '6':
            self.id = 'sh' + self.id
        else:
            self.id = 'sz' + self.id
        r = requests.get("http://api.finance.ifeng.com/akdaily/?code=" + self.id + "&type=last", proxies=proxies, timeout=2)
        if r.status_code != 200:
            print('获取历史数据异常！')
            raise Exception('This is the error message.')
        s = r.content.decode()
        text = json.loads(s)
        a = text['record']
        data = []
        start = []
        vol_s = []
        pri_Dvalue = []
        Increase = []
        close = []
        high = []
        low = []
        global df
        for i in range(len(a)):
            data.append(a[i][0])
            start.append(a[i][1])
            high.append(a[i][2])
            close.append(a[i][3])
            low.append(a[i][4])
            vol_s.append(a[i][5])
            pri_Dvalue.append(a[i][6])
            Increase.append(a[i][7])
        s_data = pd.Series[data]
        s_start = pd.Series[start]
        s_vols = pd.Series[vol_s]
        s_priDvalue = pd.Series[pri_Dvalue]
        s_Incr = pd.Series[Increase]
        s_close = pd.Series(close)
        s_high = pd.Series(high)
        s_low = pd.Series(low)
        df = pd.DataFrame({'日期', s_data, '今开', s_start, '最高', s_high, '今收', s_close, '最低', s_low
                              , '总手', s_vols, '价差', s_priDvalue, '涨幅', s_Incr})
        return df