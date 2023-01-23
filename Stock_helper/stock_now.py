import requests
import json
import pandas as pd
def stock_now_p(id):
    url=""
    if id[0]=='6':
        id='sh'+id
        url="https://hq.finance.ifeng.com/q.php?l="+id
    else:
        id = 'sz' + id
        url = "https://hq.finance.ifeng.com/q.php?l=" + id
    r = requests.get(url)
    if r.status_code!=200:
        print('实时价格异常！')

    s=r.content.decode().strip('\n').strip('var json_q=').replace(';','')
    text = json.loads(s)
    #现价
    pri_now = text[id][0]
    # 昨收
    pri_yesterday_end = text[id][1]
    #价差（今天-昨天）
    pri_Dvalue=text[id][2]
    #涨幅
    pri_Increase=text[id][3]
    #今开
    pri_today_start=text[id][4]
    #最高
    pri_high = text[id][5]
    #最低
    pri_low = text[id][6]
    #今收
    pri_today_now=text[id][7]
    #总成交量(手)
    Turnover_s=text[id][9]
    #总成交额（元）
    Turnover_y=text[id][10]
    df=pd.DataFrame({'现价',pri_now,'昨收',pri_yesterday_end,'价差',pri_Dvalue,'涨幅',pri_Increase,'今开',pri_today_start,'最高',pri_high,'最低',pri_low,'今收',pri_today_now,'总手',Turnover_s,'成交额',Turnover_y})
    return pri_now,pri_low,pri_high