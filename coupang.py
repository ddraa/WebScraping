import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

for i in range(1, 6): # 1 ~ 5 page

    url = f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        # except ad badge
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print("AD product !")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        # except apple
        if "Apple" in name:
            #print("except apple product")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text()

        # more than 50 review, 4.5 point
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "Not evaluated"
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1] # (50)
        else:
            rate_cnt = "Not evaluated"
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 50:
            #print(name, price, rate, rate_cnt)
            print(f'제품명 : {name}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}점, {rate_cnt}개의 평가')
            print(f'바로가기 : {"https://www.coupang.com"+link}')
            print("-"*100)
        