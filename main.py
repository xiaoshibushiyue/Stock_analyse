import math
import threading

from Proxy_Tools.Proxy_Helper import Proxy_Helper
from Thread_tools.DaemonThread import DaemonThread
from Thread_tools.Workthread import WorkThread

lock = threading.Lock()
#list分组----为多线程分配
def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]
D_threads=[]

#多线程封装
def th_cal(num,tf,ph):
    f = open('stock.txt')
    data = f.readlines()
    data_ = chunks(data, num)
    for i in range(num):
        #数据库判断是否数据为最新数据

        ip_port=ph.Get_IP_PORT(0)
#创建工作线程
        t=WorkThread(ip_port,data_[i],tf,ph)
        
#创建守护线程
        dem_t=DaemonThread(t,num,tf,ph)
        dem_t.start()

        D_threads.append(dem_t)
    for i in range(num):
        D_threads[i].join()
        print('守护进程结束！')


if __name__=="__main__":

    #代理池对象
    PH=Proxy_Helper(2)
    #启动线程
    th_cal(2,0,PH)
    print("结束")






