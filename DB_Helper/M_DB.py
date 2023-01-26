import pymongo
import pandas as pd
import time, datetime
class M_dbHelper:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    def __init__(self,dbname):
        self.dbname=dbname
        dblist = self.myclient.list_database_names()
        if self.dbname in dblist:
            print("数据库已存在！")
            self.mydb = self.myclient[self.dbname]
            self.mycollection=self.mydb['stock']
        else:
            self.mydb = self.myclient[self.dbname]
            self.mycollection = self.mydb['stock']


    def insert_one(self,data):
        try:
            self.mycollection.insert_one(data)
        except Exception as e:
            print(str(e))

    def insert_many(self,data):
        try:
            self.mycollection.insert_many(data)
        except Exception as e:
            print(str(e))

    def find(self):
        all=self.mycollection.find()

        list_data=[]
        for s in all:
            list_data.append(s)
        df = pd.DataFrame(list_data)
        return df
    def find_lastone(self,s_day):
        last=self.mycollection.find({"日期":s_day})
        i=0
        for x in last:
           i=i+1
        return i





