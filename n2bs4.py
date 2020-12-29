import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("div", attrs={"class":"rating_type"})
total_rate = 0
for cartoon in cartoons:
    total_rate += float(cartoon.strong.get_text())
print(total_rate / len(cartoons))