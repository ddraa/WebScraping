import requests
res = requests.get("http://google.com")
res.raise_for_status()

with open("mGoogle.html", "w", encoding="UTF-8") as f:
    f.write(res.text)
