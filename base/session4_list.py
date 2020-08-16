
# list1 = [1,2,3,4,5]
# print(list1)

# list2 = [1,2,3,4,5,"a","b","c",True]
# print(list2)

# #元组转列表
# a = (1,2,3,4,5)
# print(a)
# list3 = list(a)
# print(list3)

# list4 = list(range(1,100))
# print(list4)

# str = "abcdef"
# list5 = list(str)
# print(list5)

# #append -列表后面追加对象
# list6 = [1,2,3,4,5]
# list6.append(6)
# # print(list6)
# print(id(list6))

# #extend -列表后面追加另一个列表的多个对象
# list7 = [7,8,9]
# list6.extend(list7)
# print(id(list6))

# # print(list6)

# #+ 更extend很像，都是实现拼接两个队列的功能，加号产生一个新的列表对象，内存地址
# list8 = [7,8,9]
# list6 = list6 + list8
# print(id(list6))

# list9 = list(range(1,100))
# print(list9[1:50:3])

#count
list10 = ["a","b","c","c"]
print(list10.count("d"))

#in
print("d" in list10)



