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
metrics = finnhub_client.company_basic_financials('AAPL', 'all')
# %%
# pd.DataFrame(metrics['series']['quarterly']['cashRatio'])#.keys()
sp500

# %
My name is yash
