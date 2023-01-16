import requests
import json
def stock_now_p(id):
    url=""
    if id[0]=='6':
        id='sh'+id
        url="https://hq.finance.ifeng.com/q.php?l=sh"+id
    else:
        url = "https://hq.finance.ifeng.com/q.php?l=sz" + id
        id = 'sz' + id
    r = requests.get(url)
    if r.status_code!=200:
        print('实时价格异常！')

    s=r.content.decode().strip('\n').strip('var json_q=').replace(';','')
    text = json.loads(s)
    t=text[id][0]
    return t