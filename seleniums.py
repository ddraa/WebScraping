from selenium import webdriver

browser = webdriver.Chrome("/Users/dragon/Downloads/chromedriver")
browser.get("http://naver.com")

# click login button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# input id, pw
browser.find_element_by_id("id").send_keys("id")
browser.find_element_by_id("pw").send_keys("pw")

# login button click
browser.find_element_by_id("log.login").click()

browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_new_id")

print(browser.page_source)

browser.quit()

