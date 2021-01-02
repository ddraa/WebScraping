from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# headlessChrome 으로 표시되는 것과 다르게 일반적인 Chrome으로 접속(표시)하도록
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome("/Users/dragon/Downloads/chromedriver", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()