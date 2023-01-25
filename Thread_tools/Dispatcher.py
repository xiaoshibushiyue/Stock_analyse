import threading

lock = threading.Lock()
class Dispatcher:
    f = open('stock.txt')
    data = f.readlines()
    @staticmethod
    def Dispatch(self):
        if len(data)>0:
            global data
            lock.acquire()
            d=data.pop()
            lock.release()
            return d
        else:
            return '0'

