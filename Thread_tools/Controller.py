from Proxy_Tools.Proxy_Helper import Proxy_Helper
from Thread_tools.WorkerThread import WorkerThread


class Controller:
    t_hs=[]
    def __init__(self,tnum):
        self.tnum=tnum
    def start(self):
        ph=Proxy_Helper(self.tnum)
        for i in range(self.tnum):
            t=WorkerThread(self.tnum,ph)
            t.start()
            self.t_hs.append(t)

    def join(self):
        for i in range(self.tnum):
            self.t_hs[i].join()
        print('运行结束！')