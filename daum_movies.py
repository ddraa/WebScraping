import requests
from bs4 import BeautifulSoup



for year in range(2015, 2020):

    res = requests.get(f'https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR')
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})


    for idx, image in enumerate(images):
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)

        image_res = requests.get(image_url)
        image_res.raise_for_status

        with open(f'movie{year}_{idx+1}.jpg', "wb") as f:
            f.write(image_res.content)

        if idx >= 4: # top 5
            break