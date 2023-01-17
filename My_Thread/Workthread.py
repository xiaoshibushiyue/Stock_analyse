import time

from threading import Thread
import pandas as pd
from BBANDS import use_BBANDS_pro

#计算boll
def cal(ip_port,arr,tf=0):
    while len(arr)>0:
        s=arr.pop()
        try:
            upperband, middleband, lowerband,sp= use_BBANDS_pro(ip_port,s.strip('\n'),tf)
        except:
            return arr
        a = pd.Series(lowerband)
        b = pd.Series(middleband)
        c = pd.Series(upperband)
        low = a.values[a.size - 1]
        mid = b.values[b.size - 1]
        high = c.values[c.size - 1]
        if float(sp)<low:
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
