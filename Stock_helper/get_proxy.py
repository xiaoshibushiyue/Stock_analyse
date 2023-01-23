import requests
import json
#取num个代理ip
def GET_PROXY(num):
    num=num+5
    #http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=40d24acd2d6b3835f5584b7d975dba75&orderNo=GL20230118133056xh9QfWzp&count=
    url="http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=40d24acd2d6b3835f5584b7d975dba75&orderNo=GL20230118133056xh9QfWzp&count="+str(num)+"&isTxt=0&proxyType=1"
    r = requests.get(url)
    if r.status_code != 200:
        print('代理获取异常！')
    s = r.content.decode()
    ips = json.loads(s)
    t=ips['obj']
    return t

ip_ports=[]
#代理池
def proxy_pool_getip(num):
    num = num + 5
    #print('代理剩余'+ str(len(ip_ports)))
    if len(ip_ports)==0:
        print("添加代理ip")
        ips=GET_PROXY(num)
        for i in range(num):
            ip_ports.append(ips[i]['ip']+':'+ips[i]['port'])
        return ip_ports.pop()
    else:
        return ip_ports.pop()

