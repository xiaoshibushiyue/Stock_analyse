import math
from BBANDS import use_BBANDS
import pandas as pd
import threading
import time
threads_=[]
s_num=0
def cal_ex(st,et,s):
        try:
            #upperband, middleband, lowerband = use_BBANDS(s.strip('\n'), st='20220101', et='20230113')
            upperband, middleband, lowerband,sp= use_BBANDS(s.strip('\n'), st, et)
            a = pd.Series(lowerband)
            b = pd.Series(middleband)
            c = pd.Series(upperband)
            low = a.values[a.size - 1]
            mid = b.values[b.size - 1]
            high = c.values[c.size - 1]
            global s_num
            s_num = s_num + 1
            if sp<low:
                print(s.strip('\n'), sp)
        except:
            time.sleep(5)
            print('异常'+s.strip('\n'))
#计算boll
def cal(st,et,arr,tf=0):
    for s in arr:
        try:
            #upperband, middleband, lowerband = use_BBANDS(s.strip('\n'), st='20220101', et='20230113')
            upperband, middleband, lowerband,sp= use_BBANDS(s.strip('\n'), st, et,tf)
            a = pd.Series(lowerband)
            b = pd.Series(middleband)
            c = pd.Series(upperband)
            low = a.values[a.size - 1]
            mid = b.values[b.size - 1]
            high = c.values[c.size - 1]
            global s_num
            s_num=s_num+1
            if sp<low:
                print(s.strip('\n'), sp)
        except:
            time.sleep(1)
            print(s_num)
            cal_ex(st, et,s)

#list分组
def chunks(arr, m):
    n = int(math.ceil(len(arr) / float(m)))
    return [arr[i:i + n] for i in range(0, len(arr), n)]
#多线程封装
def th_cal(num):
    f = open('stock.txt')
    data = f.readlines()
    data_ = chunks(data, num)
    for i in range(num):
        t = threading.Thread(target=cal, args=('2022-01-05', '2023-01-16', data_[i],1,))
        threads_.append(t)

if __name__=="__main__":
    th_cal(10)
    for t in threads_:
        t.start()
    for t in threads_:
        t.join()
        print('结束'+t.getName())
    print(s_num)







