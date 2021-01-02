from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2880x1800")

browser = webdriver.Chrome("/Users/dragon/Downloads/chromedriver", options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2 # 2 sec

# 현재 문서의 높이 가져오기
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩(동기화) 대기
    time.sleep(interval)

    cur_height = browser.execute_script("return document.body.scrollHeight")
    if cur_height == prev_height:
        break # 더 이상 가져올 페이지 없음

    prev_height = cur_height
print("complete scrolling")
browser.get_screenshot_as_file("google_movie.png")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(f'except not sale movie ! {title}')
        continue

    #할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = "https://play.google.com" + movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f'제목 : {title}')
    print(f'할인 전 금액 : {original_price}')
    print(f'할인 후 금액 : {price}')
    print(f'링크 : {link}')
    print("-"*100)

browser.quit()