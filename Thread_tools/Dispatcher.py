import threading


f = open('stock.txt')
data = f.readlines()

lock = threading.Lock()
class Dispatcher:

    @staticmethod
    def Dispatch(self):
        if len(data)>0:
            lock.acquire()
            d=data.pop()
            lock.release()
            return d
        else:
            return '0'
