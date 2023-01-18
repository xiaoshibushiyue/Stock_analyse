import requests
import json
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
    pri_now=text[id][0]
    pri_low=text[id][6]
    pri_high=text[id][5]

    return pri_now,pri_low,pri_high