from selenium import webdriver

browser = webdriver.Chrome("/Users/dragon/Downloads/chromedriver")
browser.get("http://naver.com")

# click login button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# input id, pw
#browser.find_element_by_id("id").send_keys("id")
#browser.find_element_by_id("pw").send_keys("pw")


# avoid naver captcha , login
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "this.id", pw = "this.pw")

browser.execute_script(input_js)
browser.find_element_by_id("log.login").click()



# login button click
#browser.find_element_by_id("log.login").click()

# erase and input
#browser.find_element_by_id("id").clear()
#browser.find_element_by_id("id").send_keys("my_new_id")

#print(browser.page_source)

#browser.quit()

