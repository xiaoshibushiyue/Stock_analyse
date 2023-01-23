import threading
import time

from threading import Thread
import pandas as pd
from BBANDS import use_BBANDS_pro
from STOCH import use_STOCH_pro
from Stock_helper.his_data import his_dt, clear_his_data

mutex = threading.Lock()
s_num=0
#计算boll
def cal(ip_port,arr,tf=0):
    while len(arr)>0:
        s=arr.pop()
        try:
            his_dt(ip_port,s.strip('\n'),tf)
            upperband, middleband, lowerband,sp,p_low= use_BBANDS_pro(ip_port,s.strip('\n'),tf)
            k,d,j=use_STOCH_pro(ip_port,s.strip('\n'),tf)
            #一定要清除
            clear_his_data()
        except Exception as e:
            #print(str(e))
            return arr
        a = pd.Series(lowerband)
        b = pd.Series(middleband)
        c = pd.Series(upperband)
        low = a.values[a.size - 1]
        mid = b.values[b.size - 1]
        high = c.values[c.size - 1]

        #global s_num
        # mutex.acquire()
        # s_num=s_num+1
        # print('已经测试'+str(s_num)+'个')
        # mutex.release()
        if float(p_low)<=low and k.values[k.size - 1]<20 and d.values[d.size - 1]<20:
            print(s.strip('\n'), sp)
    return []



class WorkThread(Thread):

    def __init__(self, ip_port,arr,tf=0):
        Thread.__init__(self)
        self.ip_port = ip_port
        self.arr = arr
        self.tf = tf

    def run(self):
        self.result = cal(self.ip_port,self.arr,self.tf)

    def get_result(self):
        return self.result
