from threading import Thread

from My_Thread.Workthread import WorkThread
from Stock_helper.get_proxy import proxy_pool_getip


#守护线程函数
def dem_thread(t,num,tf):
    t.join()
    arr=t.get_result()
    while len(arr)>0:
        #print('剩余ip  '+str(len(arr)))
        ip_port = proxy_pool_getip(num)
        t = WorkThread(ip_port, arr, tf)
        t.start()
        t.join()
        arr = t.get_result()


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