'''
抓取邮箱的内容
1-切换窗口/切换iframe
2-等待的三种方式
3-文本框输入内容
4-点击按钮
5-页面的截屏
'''
from selenium import webdriver
from time import sleep

url = "https://email.163.com/"
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

browser.get_screenshot_as_file("d:\\2.png")

# #1-切换iframe
# browser.switch_to_frame(0)

# #等待的三种方式：1 强制等待
# # sleep(3)

# #2-隐式等待：针对页面的，声明一个最大等待时间，但如果页面加载完成，就不再等待，如果超出了最大等待时间，那就报超时错误
# # browser.implicitly_wait(5)

# #3-显示等待：正对某个页面元素的。
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# email_xpath = "/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input"
# email_input = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,email_xpath)))



# # email_input = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input")
# paw_input = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]")
# submit_btn = browser.find_element_by_id("dologin")

# # print(email_input)

# #文本框输入内容
# import secret
# email_input.send_keys("jobpool@163.com")
# paw_input.send_keys(secret.email163_password())

# sleep(2)

# #点击按钮
# submit_btn.click()

# sleep(3)

# #切换窗口
# whs = browser.window_handles
# print(whs)
# browser.switch_to_window(whs[-1])

# email_box = browser.find_element_by_xpath("/html/body/div[1]/nav/div[2]/ul/li[1]")
# email_box.click()

# sleep(2)

# emaillist = browser.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/div")
# for item in emaillist:
#     print(item.text)

sleep(3)
browser.close()
browser.quit()
