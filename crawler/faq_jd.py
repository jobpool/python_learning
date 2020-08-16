
from selenium import webdriver
from time import sleep

url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=1.his.0.0&wq=&pvid=b81a589e7007461c9288d8485f31fbce"
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

browser.implicitly_wait(5)


js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js) 
sleep(3)

els = browser.find_elements_by_class_name("gl-item")
print(len(els))

sleep(5)

browser.close()
browser.quit()