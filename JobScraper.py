#JobScraper.py

import sys
from bs4 import BeautifulSoup
from selenium import webdriver
url = "https://www.graduates24.com/"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.get(url)
html = driver.page_source
list = []
s = BeautifulSoup(html, 'html.parser')
for link in s.find_all('a'):
    href = link.get('href')
    if href:
        list.append(href)
f = open("jobs.txt", "w")
for i in range(len(list)):
    f.writelines(list[i] + "\n")