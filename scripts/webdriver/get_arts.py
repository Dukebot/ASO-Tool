from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import lxml
import re

driver = webdriver.Chrome()
driver.get("https://play.google.com/store/apps")
response = driver.execute_script("return document.documentElement.outerHTML")

soup = BeautifulSoup(response, 'lxml')
Apps = soup.find_all("div", class_="WsMG1c nnK0zc")

for app in Apps:
    print(app.text)