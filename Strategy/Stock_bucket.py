import threading

lock_kdj = threading.Lock()
lock_kdj_g = threading.Lock()
lock_boll=threading.Lock()
lock_sar=threading.Lock()
lock_trix=threading.Lock()
lock_wr=threading.Lock()
lock_roc=threading.Lock()
lock_brar=threading.Lock()

kdj=[]
kdj_g=[]
boll=[]
sar=[]
trix=[]
wr=[]
roc=[]
brar=[]
def insert_kdj(id):
    lock_kdj.acquire()
    kdj.append(id)
    lock_kdj.release()
def insert_kdj_g(id):
    lock_kdj_g.acquire()
    kdj_g.append(id)
    lock_kdj_g.release()
def insert_boll(id):
    lock_boll.acquire()
    boll.append(id)
    lock_boll.release()
def insert_sar(id):
    lock_sar.acquire()
    sar.append(id)
    lock_sar.release()
def insert_trix(id):
    lock_trix.acquire()
    trix.append(id)
    lock_trix.release()
def insert_wr(id):
    lock_wr.acquire()
    wr.append(id)
    lock_wr.release()
def insert_roc(id):
    lock_roc.acquire()
    roc.append(id)
    lock_roc.release()
def insert_brar(id):
    lock_brar.acquire()
    brar.append(id)
    lock_brar.release()
