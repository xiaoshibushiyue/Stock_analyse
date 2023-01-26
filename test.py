import pandas as pd
import requests

from DB_Helper.M_DB import M_dbHelper
from Proxy_Tools.Proxy_Helper import Proxy_Helper
from Stock_helper.History_Data import His_Data
from Stock_helper.Now_data import Now_Data

import pymongo


data=[]
ccc=len(data)
print(len(data))

r = requests.get("http://api.finance.ifeng.com/akdaily/?code=sz003043&type=last")

s = r.content.decode()


df = pd.DataFrame([{'name':'xiaos','age':13}])
newpd=pd.DataFrame([{'name':'xiaoshi','age':133}])

df=df.append(newpd,ignore_index=True)

addd=df.values[-1]
agwe=addd['age'][1]


db1=M_dbHelper('600000')
gh=db1.find_lastone()

a=1







# f = open('stock.txt')
# data = f.readlines()
# PH=Proxy_Helper(2)
# for s in data:
#     s=s.strip('\n')
#     df=His_Data(PH.Get_IP_PORT(),s).get()
#     hh=df.to_dict(orient ='records')
#     db=M_dbHelper(s)
#     db.insert_many(hh)




