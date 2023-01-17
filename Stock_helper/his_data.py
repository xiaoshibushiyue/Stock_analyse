import requests
import json
import pandas as pd
#这个端口是固定的，不用传入时间
#'http://api.finance.ifeng.com/akdaily/?code=sh603408&type=last'
def his_dt(ip_port,id,tf=0):
    proxies = {"http": ip_port}
    if id[0]=='6':
       id='sh'+id
    else:
        id = 'sz' + id
    r = requests.get("http://api.finance.ifeng.com/akdaily/?code=" + id + "&type=last", proxies=proxies)
    if r.status_code!=200:
        print('获取历史数据异常！')
        raise Exception('This is the error message.')
    s = r.content.decode()
    text = json.loads(s)
    a=text['record']
    c=[]
    for i in range(len(a)):
        c.append(a[i][3])
    s=pd.Series(c)
    return s

