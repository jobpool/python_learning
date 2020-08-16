import requests
from pyquery import PyQuery as pq
#pip install requests

resp = requests.get("http://news.163.com/special/0001386F/rank_news.html").content
doc = pq(resp)

items = doc(".left .tabBox table").eq(0)("tr").items()

news_items = []
for it in items:
    info = {}
    info["title"] = it("td").eq(0)("a").text()
    info["url"] = it("td").eq(0)("a").attr("href")
    info["counter"] = it("td").eq(1).text()

    news_items.append(info)


import common

common.dump_jsonfile("datas/news163.json",news_items)
