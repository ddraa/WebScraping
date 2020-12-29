import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
#print(soup.title.get_text())
#print(soup.a)
#print(soup.a.attrs)
#print(soup.a["href"])

#print(soup.find("a", attrs={"class":"Nbtn_upload"}))
#print(soup.find(attrs={"class":"Nbtn_upload"}))

#r1 = soup.find("li", attrs={"class":"rank01"})
#print(r1.a.get_text())
#print(r1.next_sibling)
#print(r1.next_sibling.next_sibling)
#print(r1.parent)

#r2 = r1.find_next_sibling("li")
#r1 = r2.find_previous_sibling("li")

#print(r1.find_next_siblings("li"))

webtoon = soup.find("a", text = "뷰티풀 군바리")
print(webtoon)
