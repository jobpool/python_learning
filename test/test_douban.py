'''
测试场景：
豆瓣网电影频道，验证在未登录的情况下，对某部电影进行想看评论时，要求登录才能进行。
用例设计：
1-在未登录的情况下，访问某部电影的详情页面；-利用selenium打开对应页面
2-在详情页上找到【想看】这个评论按钮，并点击； -找到【想看】这个元素，执行点击事件
3-预期结果：会弹出登录页面，要求登录。 -找到对应的登录窗口元素，证明需要登录，从而认为这个用例通过
'''

from selenium import webdriver
from time import sleep

def test_rate_unlogin():
    url = "https://movie.douban.com/subject/26754233/?from=showing"
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    borwser = webdriver.Chrome(options=options)
    #1-在未登录的情况下，访问某部电影的详情页面
    borwser.get(url)
    borwser.implicitly_wait(10)
    #2-在详情页上找到【想看】这个评论按钮，并点击
    el = borwser.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]")
    el.click()

    #3-预期结果：会弹出登录页面，要求登录
    el_login = borwser.find_element_by_name("https://movie.douban.com")
    assert el_login!=None

    sleep(2)
    borwser.close()
    borwser.quit()




