from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import lxml
import re

apple_knight = "https://play.google.com/store/apps/details?id=online.limitless.appleknight.free"
bounce_ball = "https://play.google.com/store/apps/details?id=com.raongames.bouneball"

#Parameters
url = bounce_ball
output_path = "text_files/text_file.txt"

driver = webdriver.Chrome()
driver.get(url)
response = driver.execute_script("return document.documentElement.outerHTML")

soup = BeautifulSoup(response, 'lxml')
head_text = soup.head.get_text()
body_text = soup.body.get_text()

print(soup.body)