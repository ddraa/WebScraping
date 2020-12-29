import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

res = soup.find_all("a", attrs={"class":"title"})
for re in res:
    print(re.get_text())