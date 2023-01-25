from DB_Helper.M_DB import M_dbHelper
from Proxy_Tools.Proxy_Helper import Proxy_Helper
from Stock_helper.History_Data import His_Data
from Stock_helper.Now_data import Now_Data

import pymongo

class test1:
    a = ''
    def ss(self):
        pass
    def aaa(self):
        def bbb():
            global a
            a = 1

        bbb()
        return a


c=test1()
b=c.aaa()
print(b)
db1=M_dbHelper('600000')

gh=db1.find()

# f = open('stock.txt')
# data = f.readlines()
# PH=Proxy_Helper(2)
# for s in data:
#     s=s.strip('\n')
#     df=His_Data(PH.Get_IP_PORT(),s).get()
#     hh=df.to_dict(orient ='records')
#     db=M_dbHelper(s)
#     db.insert_many(hh)




