from Thread_tools.WorkerThread import WorkerThread


class Controller:
    t_hs=[]
    def __init__(self,tnum,tf):
        self.tf=tf
        self.tnum=tnum
    def start(self):
        for i in range(self.tnum):
            t=WorkerThread(self.tf)
            t.start()
            self.t_hs.append(t)

    def join(self):
        for i in range(self.tnum):
            self.t_hsp[i].join()
        print('运行结束！')