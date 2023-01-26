import threading


f = open('stock.txt')
data = f.readlines()
num=0
lock = threading.Lock()
class Dispatcher:


    @staticmethod
    def Dispatch(self):
        lock.acquire()
        if len(data)>0:
            global num

            num=num+1
            d=data.pop()
            print('提取：'+str(num))
            lock.release()
            return d.strip('\n')

        else:
            lock.release()
            return '0'
