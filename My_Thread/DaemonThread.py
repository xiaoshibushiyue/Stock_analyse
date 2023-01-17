from threading import Thread

from My_Thread.Workthread import WorkThread
from Stock_helper.get_proxy import proxy_pool_getip


#守护线程函数
def dem_thread(t,num,tf):
    t.join()
    while len(t.get_result())>0:
        ip_port = proxy_pool_getip(num)
        t1 = WorkThread(ip_port, t.get_result(), tf)
        t = t1
        t1.start()
        t1.join()


class DaemonThread(Thread):
    def __init__(self, t,num,tf):
        Thread.__init__(self)
        self.t = t
        self.num = num
        self.tf = tf
    def run(self):
        self.result = dem_thread(self.t,self.num,self.tf)

    def get_result(self):
        return self.result