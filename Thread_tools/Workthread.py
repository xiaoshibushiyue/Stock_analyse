import threading

from threading import Thread
import pandas as pd
from Talib_func.BBANDS import use_BBANDS_pro
from Talib_func.STOCH import use_STOCH_pro

mutex = threading.Lock()
s_num=0
#计算boll
def cal(ip_port,arr,tf,ph):
    while len(arr)>0:
        s=arr.pop()
        try:
            upperband, middleband, lowerband,sp,p_low= use_BBANDS_pro(ip_port,s.strip('\n'),tf)
            k,d,j=use_STOCH_pro(ip_port,s.strip('\n'),tf)
        except Exception as e:
            #print(str(e))
            mutex.acquire()
            ph.Add_waste_ip(ip_port)
            mutex.release()
            return arr
        a = pd.Series(lowerband)
        b = pd.Series(middleband)
        c = pd.Series(upperband)
        low = a.values[a.size - 1]
        mid = b.values[b.size - 1]
        high = c.values[c.size - 1]

        global s_num
        mutex.acquire()
        s_num=s_num+1
        print('已经测试'+str(s_num)+'个')
        mutex.release()
        if float(p_low)<=low and k.values[k.size - 1]<20 and d.values[d.size - 1]<20:
            print(s.strip('\n'), sp)
    return []



class WorkThread(Thread):

    def __init__(self, ip_port,arr,tf,ph):
        Thread.__init__(self)
        self.ip_port = ip_port
        self.arr = arr
        self.tf = tf
        self.ph=ph
    def run(self):
        self.result = cal(self.ip_port,self.arr,self.tf,self.ph)

    def get_result(self):
        return self.result
