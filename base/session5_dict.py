# #字典的定义
# d1 = {"a":1,"b":2}
# print(type(d1),d1)

# #键值是唯一的
# d2 = {"a":1,"b":2,"a":3}
# print(d2)

# #键值为字符串、数字、元组，不能是列表，要求不可变数据类型
# d3 = {"a":1,2:"b",(3,4):"c"}
# print(d3)

# #访问字典
# d4= {"a":1,"b":2}
# # print(d4["c"])
# # print(d4.get("c",0))
# print(d4)
# print(d4.pop("b"))
# print(d4)

# #添加键值到字典
# d5 =  {"a":1,"b":2}
# d5["c"] = 3
# print(d5)

# #修改字典
# d6 =  {"a":1,"b":2}
# # d6["b"]=3
# # print(d6)
# d7 = {"a":10,"b":20,"c":30}
# # print(id(d6))
# d6.update(d7)
# # print(id(d6))
# print(d6)

#删除
# d8 = {"a":1,"b":2}
# # del(d8["b"])
# # print(d8)
# d8.pop("b")
# print(d8)

d9 = {"a":1,"b":2}
# print(list(d9.keys()))
# print(list(d9.values()))

# if "c" in d9:
#     print(True)
# else:
#     print(False)

if d9.get("c") is not None:
    print(True)
else:
    print(False)

