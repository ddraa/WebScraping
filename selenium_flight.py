from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/Users/dragon/Downloads/chromedriver")
browser.maximize_window()
browser.get("https://flight.naver.com/flights/")

browser.find_element_by_link_text("가는날 선택").click()
browser.find_elements_by_link_text("13")[0].click() # from jan 13
browser.find_elements_by_link_text("14")[1].click() # to feb 14

browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click() # click jeju
browser.find_element_by_link_text("항공권 검색").click()

try:
    # 로딩 창 같은 경우를 대비해 최대 10초까지, 감지된 element가 있을때까지 체크
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text) # print text
finally:
    browser.quit()