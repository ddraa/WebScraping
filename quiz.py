import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for i, row in enumerate(data_rows):
    columns = row.find_all("td")

    print(f'{"="*8} 매물 {i + 1} {"="*8}')
    print(f'거래 : {columns[0].get_text()}')
    print(f'면적 : {columns[1].get_text()}')
    print(f'가격 : {columns[2].get_text()}')
    print(f'동 : {columns[3].get_text()}')
    print(f'층 : {columns[4].get_text()}')