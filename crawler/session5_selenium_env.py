#Selenium是一个用电脑模拟人操作浏览器网页，可以实现自动化，测试等
#1-已经安装好Python(3)
#2-安装selenium：pip install selenium
#3-需要配置好浏览器驱动：Firefox浏览器：geckodriver；Chrome：chromedriver；Edge：MicrosoftWebDriver
#下载地址：http://chromedriver.storage.googleapis.com/index.html，找到对应版本
#driver拷贝到当前python运行环境对应的目录下，即与python.exe文件同一个目录下

#4-验证selenium环境配置好
from selenium import webdriver
from time import sleep

#如果出现【“Chrome Automation Extension”崩溃了】的提示，用以下方式：
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")  #非沙盒模式

#多种浏览器启动方式
browser = webdriver.Chrome(chrome_options=chrome_options)

#利用browser打开网页
# sleep(1)
browser.get("https://www.baidu.com")

sleep(5)
browser.quit()
