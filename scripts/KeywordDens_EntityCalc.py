import requests
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
import time
import io
from fake_useragent import UserAgent


def load_from_external_CSV():
    excsv = requests.get('CSV_URL').content
    crawldf = pd.read_csv(io.StringIO(excsv.decode('utf-8')))
    addresses = crawldf['Address'].tolist()
    return addresses

def load_from_local_CSV():
    crawldf = pd.read_csv('LOCAL_PATH_TO_CSV') 
    addresses = crawldf['Address'].tolist()
    return addresses


#Load from Python list
addresses = ['URL1','URL2','URL3']

ua = UserAgent()
 
headers = {
    'User-Agent': ua.chrome
}