from Proxy_Tools.Proxy_Helper import Proxy_Helper
from Stock_helper.History_Data import His_Data
from Stock_helper.Now_data import Now_Data

a=His_Data('36.44.75.170:19740','600000')
a1=a.get()
print(a1)

