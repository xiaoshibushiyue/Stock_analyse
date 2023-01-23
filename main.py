import math
import threading

from My_Thread.DaemonThread import DaemonThread
from My_Thread.Workthread import WorkThread
from Stock_helper.get_proxy import proxy_pool_getip, Set_pool_num


#list分组----为多线程分配
def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]
D_threads=[]

#多线程封装
def th_cal(num,tf):
    th_num=num
    f = open('stock.txt')
    data = f.readlines()
    data_ = chunks(data, num)

    for i in range(num):
        ip_port=proxy_pool_getip(num)
        t=WorkThread(ip_port,data_[i],tf)
        t.start()

#创建守护线程
        dem_t=DaemonThread(t,num,tf)
        dem_t.start()
        D_threads.append(dem_t)
    for i in range(num):
        D_threads[i].join()
        print('守护进程结束！')


if __name__=="__main__":
    #设置线程数
    Set_pool_num(2)
    #启动线程
    th_cal(2,0)
    print("结束")






