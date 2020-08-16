#requests  urllib
#pip install 包名称
import requests

#get
# url = "http://news.163.com/special/0001386F/rank_news.html"
# resp = requests.get(url)
# # print("status:{},reason:{}".format(resp.status_code,resp.reason))
# print(resp.text)

#headers
# url = "http://news.163.com/special/0001386F/rank_news.html"
# resp = requests.get(url,headers = {"User_Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36 Edg/84.0.522.50"})
# print(resp.text)

#post
# url = "http://httpbin.org/post"
# resp =requests.post(url,data={"name":"jobpool","email":"jobpool@163.com"})
# print(resp.text)

# #proxy
# url = "http://www.baidu.com"
# proxy_params = {"http":"http://165.225.56.16:10605"}
# resp = requests.get(url,proxies = proxy_params)
# print(resp.text)

#图片、视频
# url = "https://img9.doubanio.com/view/photo/l/public/p2588064256.webphttps://music.douban.com/artists/player/?sid=759346,743765,723146,756991,203057,206022&source=index"
# resp = requests.get(url)
# with open("datas/1.jpg",mode="wb") as f:
#     f.write(resp.content)
    
url = "https://key003.ku6.com/yugaopian/d3a04e17efbb4895b7e21d53beac529f.mp4"
resp = requests.get(url)
with open("datas/1.mp4",mode="wb") as f:
    f.write(resp.content)

