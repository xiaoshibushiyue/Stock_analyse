import threading

lock_kdj = threading.Lock()
lock_kdj_g = threading.Lock()
lock_boll=threading.Lock()
lock_sar=threading.Lock()
lock_trix=threading.Lock()
lock_wr=threading.Lock()
lock_roc=threading.Lock()
lock_brar=threading.Lock()
lock_macd=threading.Lock()

kdj=[]
kdj_g=[]
boll=[]
sar=[]
trix=[]
wr=[]
roc=[]
brar=[]
macd=[]
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
def insert_macd(id):
    lock_macd.acquire()
    macd.append(id)
    lock_macd.release()
    #
    # kdj = []
    # kdj_g = []
    # boll = []
    # sar = []
    # trix = []
    # wr = []
    # roc = []
    # brar = []
    # macd = []
def print_result():
    print('------------------kdj----------------------')
    for value in kdj:
        print(value)
    print('------------------kdj_g----------------------')
    for value in kdj_g:
        print(value)
    print('------------------boll----------------------')
    for value in boll:
        print(value)
    print('------------------sar----------------------')
    for value in sar:
        print(value)
    print('------------------trix----------------------')
    for value in trix:
        print(value)
    print('------------------wr----------------------')
    for value in wr:
        print(value)
    print('------------------roc----------------------')
    for value in roc:
        print(value)
    print('------------------brar----------------------')
    for value in brar:
        print(value)
    print('------------------macd----------------------')
    for value in macd:
        print(value)
