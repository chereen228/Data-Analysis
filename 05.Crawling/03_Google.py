import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.google.com')
iver = webdriver.Chrome('./chromedriver')
driver.get('http://www.google.com')
time.sleep(0.5)         # 0.5초 기다림

search_box = driver.find_element_by_css_selector('input.gLFyf.gsfi')
search_box.send_keys('ChromeDriver')
search_box.send_keys(Keys.ENTER)    #Keys.RETURN
time.sleep(1)

div = driver.find_elements_by_css_selector("div#rso>div.g")
len(div)

for div in divs:
    title = div.find_element_by_css_selector('.LC20lb.DKV0Md').text
    content = div.find_element_by_css_selector('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc').text
    print(title)
    print(content)

