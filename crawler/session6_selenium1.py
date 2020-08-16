#1-模拟浏览器打开网页

url = "http://news.163.com/special/0001386F/rank_news.html"
browser = webdriver.Chrome()
browser.get(url)

#2-特殊情况下的处理

# #如果出现【“Chrome Automation Extension”崩溃了】的提示，用以下方式：
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")  #非沙盒模式

# #多种浏览器启动方式
# browser = webdriver.Chrome(chrome_options=chrome_options)

#3-通过多种方式获取element
'''
find_element_by_id()
find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_xpath()
find_element_by_css_selector()
'''
# el = browser.find_element_by_id("top")
# print(type(el))
# print(el.get_attribute("alt"))
# print(browser.title)
# print(browser.current_url)
# el = browser.find_element_by_name("author")
# print(el.get_attribute("content"))
# els= browser.find_elements_by_tag_name("table")
# print("els:",len(els))
# el = browser.find_element_by_link_text("最新")
# print(el.text)

# el = browser.find_element_by_partial_link_text("最")
# print(el.text)

# el = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[1]")
# print(el.text)

# el = browser.find_element_by_css_selector(".nav_channel")
# print(el.text)