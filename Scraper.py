import requests, sys, urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

sys.stdout.reconfigure(encoding='utf-8')
url = "https://www.zabursaries.co.za/computer-science-it-bursaries-south-africa/"
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
list = []
# r = requests.get(url)
s = BeautifulSoup(html, 'html.parser')
for link in s.find_all('a'):
    href = link.get('href')
    if href:
        list.append(href)
f = open("sites.txt", "w")
for i in range(len(list)):
    f.writelines(list[i] + "\n")
#     href = link.get('href')
#     if href:
#         f.write(href)
# try:
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     html_content = data.decode('utf-8')
#     print(html_content)
# except Exception as e:
#     print("Error: ", e)

# print(s.prettify().encode('utf-8', 'ignore').decode('utf-8'))
# s = soup.find('div', class_='entry-content')
# print(s.find_all('p'))
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://google.co.in / search?q = geeksforgeeks")