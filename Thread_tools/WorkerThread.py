from threading import Thread
import pandas as pd
from Proxy_Tools.Proxy_Helper import Proxy_Helper
from Talib_func.BBANDS import use_BBANDS_pro
from Talib_func.STOCH import use_STOCH_pro
from Thread_tools.Dispatcher import Dispatcher


class WorkerThread(Thread):
    upperband, middleband, lowerband, k, d, j, sp, p_low = ''
    ip_times=0
    def __init__(self, tf):
        Thread.__init__(self)
        self.time = 0
        self.id = None
        self.ip = Proxy_Helper.Get_IP_PORT()
        self.tf = tf
    def run(self):
        while True:
            self.id = Dispatcher.Dispatch()
            while self.id!='0':
                self.cal(self.id)
    def get_result(self):
        return self.result

    def ip_record(self,ip,sf):
        self.ip=ip
        if self.time>=3:
            self.ip=Proxy_Helper.Get_IP_PORT()
            self.time = 0
        if sf!='s':
            self.time=self.time+1
    def cal(self,id):
        def strategy():
            try:
                global upperband, middleband, lowerband, k, d, j, sp, p_low
                upperband, middleband, lowerband, sp, p_low = use_BBANDS_pro(self.ip, id.strip('\n'),self.tf)
                k, d, j = use_STOCH_pro(self.ip, id.strip('\n'),self.tf)
                return 0
            except Exception as e:
                self.ip_record(self.ip, 'f')
                return 1
        while strategy() != 0:
            strategy()
        a = pd.Series(lowerband)
        b = pd.Series(middleband)
        c = pd.Series(upperband)
        low = a.values[a.size - 1]
        mid = b.values[b.size - 1]
        high = c.values[c.size - 1]

        # global s_num
        # mutex.acquire()
        # s_num = s_num + 1
        # print('已经测试' + str(s_num) + '个')
        # mutex.release()
        if float(p_low) <= low and k.values[k.size - 1] < 20 and d.values[d.size - 1] < 20:
            print(id.strip('\n'), sp)
