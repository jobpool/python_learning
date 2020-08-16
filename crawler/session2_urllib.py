from urllib import request

url = "http://news.163.com/special/0001386F/rank_news.html"

# with request.urlopen(url) as p:
#     # print(p.status,p.reason)
#     content = p.read()
#     print("content>>",content.decode("GBK"))

#headers
# req = request.Request(url)
# req.add_header("User_Agent","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36 Edg/84.0.522.50")
# with request.urlopen(req) as p:
#     for k,v in p.getheaders():
#         print("{}:{}".format(k,v))

#POST
# from urllib import parse
# url = "http://httpbin.org/post"
# datas = {"Name":"Jobpool","Email":"jobpool@163.com"}
# post_datas = parse.urlencode(datas).encode("utf-8")
# req = request.Request(url,method="POST",data=post_datas)
# req.add_header("User_Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.50")
# with request.urlopen(req) as p:
#     content = p.read()
#     print("content>>",content.decode("utf-8"))

#Handler
#需要代理的时候
url = "http://www.baidu.com"
proxy_han = request.ProxyHandler({"http":"http://110.43.49.185:8080"})
# proxy_auth = request.ProxyBasicAuthHandler()
# proxy_auth.add_password("","","username","passowrd")
opener = request.build_opener(proxy_han)
with opener.open(url) as p:
    content = p.read()
    print("content>>",content.decode("utf-8"))


