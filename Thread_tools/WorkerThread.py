from threading import Thread
import pandas as pd
from Stock_helper.All_Data import All_Data
from Talib_func.overlap_studies.BBANDS import  use_BBANDS
from Talib_func.STOCH import  use_STOCH
from Thread_tools.Dispatcher import Dispatcher

class WorkerThread(Thread):

    ip_times=0
    def __init__(self,t_num,ph):
        Thread.__init__(self)
        self.time = 0
        self.id = None
        self.ph=ph

        self.ip = ph.Get_IP_PORT()
        print('线程初始化获取ip'+self.ip)
        self.df=pd.DataFrame()
    def run(self):
        disp = Dispatcher()
        self.id = disp.Dispatch(disp)
        while self.id!='0':
            self.cal(self.id)
            self.id = disp.Dispatch(disp)
    def get_result(self):
        return self.result

    def ip_record(self,ip,sf):
        self.ip=ip
        if self.time>=3:
            print('线程废弃，获取新ip')
            self.ip=self.ph.Get_IP_PORT()
            self.time = 0
        if sf!='s':
            self.time=self.time+1
    def cal(self,id):
        self.df=pd.DataFrame()
        def Get_data():
            try:
                #print('开始测试')
                all_data=All_Data(self.ip,self.id)
                self.df= all_data.GET()
                #print("测试成功")
                return 0
            except Exception as e:
                self.ip_record(self.ip, 'f')
                #print("异常")
                return 1

        while Get_data()!=0:
            continue

        #策略
        def strategy():
            upperband, middleband, lowerband, = use_BBANDS(self.df['今收'])
            p=self.df.values[-1]
            try:
                p_low=p[int(4+1)]
                p_high=p[int(2+1)]
                p_now=p[int(3+1)]
                k, d, j = use_STOCH(self.df['最高'],self.df['最低'],self.df['今收'])
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
                    print(id.strip('\n'), p_now)
            except Exception as e:
                print(str(e))

        strategy()


