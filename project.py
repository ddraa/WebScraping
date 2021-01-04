import requests
import re
from bs4 import BeautifulSoup


def createSoup(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrapeWeather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = createSoup(url)

    curtemp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    MIN = soup.find("span",attrs={"class":"min"}).get_text()
    MAX = soup.find("span",attrs={"class":"max"}).get_text()

    sensible = soup.find("span",attrs={"class":"sensible"}).get_text()
    morning = soup.find("span",attrs={"class":"point_time morning"}).get_text().strip()
    afternoon = soup.find("span",attrs={"class":"point_time afternoon"}).get_text().strip()

    datas = soup.find("dl", attrs={"class":"indicator"}).find_all("dd")

    print(cast)
    print(f'현재 {curtemp} (최저 {MIN} / 최고 {MAX})')
    print(f'오전 {morning} / 오후 {afternoon}')
    print(f'미세먼지 {datas[0].get_text()}, 초미세먼지 {datas[1].get_text()}')
    print()
    # info = soup.find("ul", attrs={"class":"info_list"}).find_all("li")
    # for i in range(len(info)):
    #     print(info[i].get_text())

def print_news(index, title, link):
    print(f'{index + 1}. {title}')
    print(f'링크 : {link}')

def scrapeNews():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = createSoup(url)
    newlist = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit = 3) 
    for index, news in enumerate(newlist):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()
        

def scrapeITNews():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = createSoup(url)
    newlist = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit = 3)
    for index, news in enumerate(newlist):
        temp = news.find_all("dt")
        title = temp[1].get_text().strip()
        link = news.find("a")["href"]
        print_news(index, title, link)
    print()


def scrapeEnglish():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = createSoup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("영어지문")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())

    print("한글지문")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())


if __name__ == "__main__":
    scrapeWeather()
    scrapeNews()
    scrapeITNews()
    scrapeEnglish()