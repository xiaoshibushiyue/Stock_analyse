import threading
from threading import Thread

from Thread_tools.Workthread import WorkThread

lock = threading.Lock()
#守护线程函数
def dem_thread(t,num,tf,ph):
    t.join()
    arr=t.get_result()
    while len(arr)>0:
        #print('剩余ip  '+str(len(arr)))
        lock.acquire()
        ip_port = ph.Get_IP_PORT(0)
        lock.release()
        t = WorkThread(ip_port, arr, tf)
        t.start()
        t.join()
        arr = t.get_result()


class DaemonThread(Thread):
    def __init__(self, t,num,tf,ph):
        Thread.__init__(self)
        self.t = t
        self.num = num
        self.tf = tf
        self.ph=ph
    def run(self):
        self.result = dem_thread(self.t,self.num,self.tf,self.ph)

    def get_result(self):
        return self.result