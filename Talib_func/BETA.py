import talib as tb
# 贝塔系数
# 个别股票或股票基金相对于整个股市的价格波动情况

# β=1，表示该单项资产的风险收益率与市场组合平均风险收益率呈同比例变化，其风险情况与市场投资组合的风险情况一致；
# ◆ β>1，说明该单项资产的风险收益率高于市场组合平均风险收益率，则该单项资产的风险大于整个市场投资组合的风险；
# ◆ β<1，说明该单项资产的风险收益率小于市场组合平均风险收益率，则该单项资产的风险程度小于整个市场投资组合的风险。
from Base_data import Get_stock_data
def use_BETA(high,low):
    #df = Get_stock_data(id, st, et)
    a = tb.BETA(high,low)
    return a