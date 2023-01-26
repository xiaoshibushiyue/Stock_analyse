#代理类
import json
import  time
import requests
import threading


lock=threading.Lock()
#暂时不解决ip浪费的问题
class Proxy_Helper:
    #代理池中的线程数---因为代理服务商有代理调用频率的限制，所以只能提前存储好一定数量的代理
    __proxy_num=0
    #代理池--记录ip和获取时间(5分钟失效)
    __proxy_ips=[]
    #废弃池
    __proxy_ips_useless=[]
    def __init__(self,t_num):
        self.__proxy_num=t_num

    #设置代理最小取备数
    def Set_Proxy_num(num):
       Proxy_Helper.__proxy_num=num
    def __Get_Pro_num(self):
       return self.__proxy_num

#从代理商获取ip
    def Get_ips(self):
        Proxy_Helper.__proxy_num = Proxy_Helper.__proxy_num + 2
        url = "http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=40d24acd2d6b3835f5584b7d975dba75&orderNo=GL20230118133056xh9QfWzp&count=" + str(
            Proxy_Helper.__proxy_num) + "&isTxt=0&proxyType=1"
        r = requests.get(url)
        if r.status_code != 200:
            print('代理获取异常！')
            return
        s = r.content.decode()
        if s.__contains__('error'):
            print('代理用完了！')
            return
        ips = json.loads(s)
        t = ips['obj']
        t1=[]
        for i in range(Proxy_Helper.__proxy_num):
            t1.append(t[i]['ip']+':'+t[i]['port'])
        self.__proxy_ips=t1


#获取ip mode为获取模式 0为非节省模式 1为节省模式
    def Get_IP_PORT(self,mode=0):
        if mode==0:
            ip=''
            lock.acquire()
            if len(self.__proxy_ips)==0:
                self.Get_ips()
            ip=self.__proxy_ips.pop()
            lock.release()
            return ip

        if mode==1:
            if len(self.__proxy_ips_useless)!=0:
                return self.__proxy_ips_useless.pop()
            else:
                if len(self.__proxy_ips) == 0:
                    self.Get_ips()
                return self.__proxy_ips.pop()
#记录废弃ip
    def Add_waste_ip(self,ip_port):
        self.__proxy_ips_useless.append(ip_port)


