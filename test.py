from BBANDS import use_BBANDS_pro
from STOCH import use_STOCH
from Stock_helper.get_proxy import GET_PROXY
from Stock_helper.his_data import his_dt
from Stock_helper.stock_now import stock_now_p
import pandas as pd

import time

from threading import Thread

se_close ,se_high,se_low= his_dt('115.209.248.6:17894','000001',0)
use_STOCH(se_high,se_low,se_close)
