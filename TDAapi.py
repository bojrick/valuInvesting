#%%
import imp
from multiprocessing.connection import Client
import pandas as pd
from pyvirtualdisplay import Display
import tda
import atexit
import os

# import chromedriver_binary  # Adds chromedriver binary to path

os.chdir("/mnt/c/Users/bojri/Desktop/valuInvesting/")
API_KEY = open("apiKey",'r').read()
REDIRECT_URI = 'https://localhost:8080/'
TOKEN_PATH = 'refreshToken.json'
SP500_URL = "https://tda-api.readthedocs.io/en/latest/_static/sp500.txt"


def make_webdriver():
    # Import selenium here because it's slow to import
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Ensure GUI is off
    # chrome_options.add_argument("--no-sandbox")
    # webdriver_service = Service("/mnt/c/Users/bojri/Desktop/valuInvesting/chromedriver")
    driver = webdriver.Chrome(options=chrome_options)
    # atexit.register(lambda: driver.quit())
    return driver

# driver = make_webdriver()
# driver.get("www.google.com")
# driver.quit()
# Create a new client
client = tda.auth.client_from_login_flow(
    api_key = API_KEY,
    redirect_url = REDIRECT_URI,
    token_path = TOKEN_PATH,
    webdriver = make_webdriver())

# %%
# get stock fundamental data
import httpx
sp500 = httpx.get(
    SP500_URL, headers={
        "User-Agent": "Mozilla/5.0"}).read().decode().split()

response = client.search_instruments(sp500[:10], client.Instrument.Projection.FUNDAMENTAL)
# %%
pd.DataFrame.from_dict(response.json()['A']['fundamental'],orient='index')
# sp500
# %%
client.get_account("232046748").json()
# %%
