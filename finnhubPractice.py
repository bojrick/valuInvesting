#%%
import finnhub
import pandas as pd
import httpx
SP500_URL = "https://tda-api.readthedocs.io/en/latest/_static/sp500.txt"
finnhub_client = finnhub.Client(api_key="c84nqfqad3i9u79hcafg")
sp500 = httpx.get(
    SP500_URL, headers={
        "User-Agent": "Mozilla/5.0"}).read().decode().split()
# sp500

# %%
from functools import reduce
def getMetricTable(ticker):
    metrics = finnhub_client.company_basic_financials(ticker, 'all')
    # return metrics
    tempLs = []
    for metric in metrics['series']['quarterly'].keys():
        tempLs.append(pd.DataFrame(metrics['series']['quarterly'][metric]).rename({"v":metric},axis=1))
    return reduce(lambda left,right: pd.merge(left,right,on='period'), tempLs)
    
# dfs = [df1, df2, df3, df4, df5, df6]
    # df_final = 
    # tempDf = pd.concat(tempLs,axis=1).reset_index().melt('index')
    # tempDf['Ticker'] = ticker
    # return tempDf
# sp500
# metrics
# %
# %%
import time
finalLs = []
for ticker in sp500:
    try:
        finalLs.append(getMetricTable(ticker))
        print(f"{ticker} Done!")
        time.sleep(2)
    except:
        print(ticker,"Data Not Found")
        continue

# %%
getMetricTable("CBRE")
# %%
final
# %%
