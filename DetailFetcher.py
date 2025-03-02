#counter programme for the bursaries
import re, threading
from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys, time


file = open("sites.txt", "r")
myList = file.readlines()
driver = webdriver.Chrome()

# for line in list:
#     http = line.find(".za/")
#     print(line)

idDict = dict()

def makeCategories():
    categories = []
    category_set =set()
    for i in range(7, 23):
        line = myList[i]
        za = line.find(".za/")
        category = line[za+4:]
        categories.append(category[:category.find("/")])
    for category in categories:
        category_set.add(category)
    return category_set


# for i in range(len(category_set)):
#     idDict[i] = category_set[i]

def findBursaries(category):
    myset = list()
    for line in myList:
        if category in line:
            myset.append(line)
    return list(set(myset))

def process_category(category):
    aList = findBursaries(category)
    with open(f"{category}.txt", "w", encoding="utf-8") as f:
        for line in aList:
            f.write(line)
            newlist = list()
            time.sleep(3)
            driver.get(line)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            div_tag = soup.find("div", id="content")
            text_content = div_tag.get_text(strip=False)
            newlist.append(text_content)
            newlist.append(("*******\n"))
            for par in newlist:
                f.writelines(par)
    
def main():
    category_set = makeCategories()
    threads = list()

    for category in category_set:
        process_category(category)
    #     thread = threading.Thread(target=process_category, args=(category,))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()  

if __name__ == "__main__":
    main()
