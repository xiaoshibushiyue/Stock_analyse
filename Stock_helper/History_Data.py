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
        r = requests.get("http://api.finance.ifeng.com/akdaily/?code=" + self.id + "&type=last", proxies=proxies, timeout=20)
        if r.status_code != 200:
            print('获取历史数据异常！')
            raise Exception('This is the error message.')
        s = r.content.decode()
        if s=='{"record":{}}':
            print('返回了空数据')
            raise Exception('This is the error message.')
        #'{"record":{}}'
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
        #这里没有一个成交量 只有一个总手
        df = pd.DataFrame({'日期':data, '今开': start, '最高':high, '今收':close, '最低': low
                              , '总手': vol_s, '价差': pri_Dvalue, '涨幅': Increase})

        return df