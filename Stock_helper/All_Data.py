import pandas as pd
from chinese_calendar import is_workday, is_holiday
import chinese_calendar as calendar
import time, datetime

from DB_Helper.M_DB import M_dbHelper
from Stock_helper.Now_data import Now_Data
from Stock_helper.History_Data import His_Data


def is_weekday(date):
    '''
    判断是否为工作日
    '''
    Y = date.year
    M = date.month
    D = date.day
    april_last = datetime.date(Y, M, D)
    return is_workday(april_last)


def is_holidays(date):
    '''
    判断是否为节假日
    '''
    Y = date.year
    M = date.month
    D = date.day
    april_last = datetime.date(Y, M, D)
    return is_holiday(april_last)


def is_festival(date):
    """
    判断是否为节日
    注意：有些时间属于相关节日的调休日也会显示出节日名称，可参考源码https://pypi.org/project/chinesecalendar/
    """
    Y = date.year
    M = date.month
    D = date.day
    april_last = datetime.date(Y, M, D)
    on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
    return on_holiday, holiday_name
#返回上一个交易日的日期--字符串
def last_Tradingday():
    data = datetime.datetime.now()
    data=sub_day(data,1)
    while is_weekday(data)==False:
        data = sub_day(data,1)
    Y = data.year
    M = data.month
    D = data.day

    str_data = ''
    if data.month < 10:
        str_data = str(Y) + '-' + '0' + str(M)
    else:
        str_data = str(Y)
    if data.day < 10:
        str_data = str_data + '-' + '0' + str(D)
    else:
        str_data = str_data + '-' + str(D)

    return str_data

def sub_day(data,dayss):

    delta = datetime.timedelta(days=dayss)
    data = data - delta
    return data
#判断是否是交易时间
def isTrading_day_time():
    data = datetime.datetime.now()
    if is_weekday(data) == False:
        return False
    else:
        #判断是不是交易时段
        if data.hour>9 and data.minute>30:
            if data.hour<15:
                return True
        return  False
def Get_data_now():
    data = datetime.datetime.now()
    Y = data.year
    M = data.month
    D = data.day
    str_data = ''
    if data.month < 10:
        str_data = str(Y) + '-' + '0' + str(M)
    else:
        str_data = str(Y)
    if data.day < 10:
        str_data = str_data + '-' + '0' + str(D)
    else:
        str_data = str_data + '-' + str(D)
    return str_data

class All_Data:
    def __init__(self,ip_port,id):
        self.ip_port=ip_port
        self.id=id
    def GET(self):
        global df, df_his,df_now
        #获取历史数据
        m_db=M_dbHelper(self.id)
        if m_db.find_lastone(last_Tradingday()) > 0:
            df_his = m_db.find()
        else:
            his=His_Data(self.ip_port, self.id)
            df_his = his.get()
            #更新历史数据
            hh = df_his.to_dict(orient='records')

            m_db.insert_many(hh)

        #判断是否为交易时段
        if isTrading_day_time():
            df_now = Now_Data(self.id)
        else:
            df_now = None
        #融合数据 现价当作今日收盘价
        #历史
        #日期':data, '今开': start, '最高':high, '今收':close, '最低': low, '总手': vol_s, '价差': pri_Dvalue, '涨幅': Increase
        #实时
        #'现价':pri_now, '昨收':pri_yesterday_end, '价差':pri_Dvalue, '涨幅': pri_Increase,'今开':pri_today_start, '最高': pri_high, '最低': pri_low, '今收': pri_today_now, '总手':Turnover_s, '成交额':Turnover_y

        if df_now!=None:
            new_pd=pd.DataFrame([{'日期':Get_data_now(),'今开':df_now.at(0,'今开'),'最高':df_now.at(0,'最高'),'今收':df_now.at(0,'现价'),'最低':df_now.at(0,'最低'),'总手':df_now.at(0,'总手'),'价差':df_now.at(0,'价差'),'涨幅':df_now.at(0,'涨幅')}])
            df=df_his.append(new_pd,ignore_index=True)
        else:
            return df_his
        return df




