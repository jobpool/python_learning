#先安装：pip install pyquery
from pyquery import PyQuery as pq
# import requests

# url = "http://news.163.com/special/0001386F/rank_news.html"
# resp = requests.get(url)
# doc = pq(resp.text)
# # print(type(doc))
# print(doc("head"))


url = "http://news.163.com/special/0001386F/rank_news.html"
doc = pq(url=url)
# print(type(doc))
# print(doc("head"))
#通过id #idname
# print(doc("#top"))
#通过class name .classname
# print(doc(".channel2019_logo"))

#获取对象的属性，attr
# print(doc(".channel2019_logo").attr("alt"))

#获取对象的文本内容 text()
# print(doc("table").eq(0).text())

#Dom操作
#1-添加、删除html的样式、属性
html = '''<html>
            <body>
                <div>第一个<a>link</a></div>
                <div>第二个</div>
            </body>
            </html>'''
doc = pq(html)
# # print(type(doc))
# doc("div").eq(0).add_class("myclassname")
# doc("div").eq(0).attr("alt","第一个")
# doc("div").eq(0).css("width","30px")
# print(doc)
# doc("div").eq(0).remove_class("myclassname")
# doc("div").eq(0).remove_attr("alt")
# print(doc)

#获取对象的子对象/父对象/兄弟对象
div1 = doc("div").eq(0)
# print(div1)
# print(div1.children())
# print(div1.parents())
# print(div1.siblings())
