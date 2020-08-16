
# def fun1():
#     print("这时一个函数")

# fun1()

# def fun2(x,y):
#     print("x+y=",x+y)

# fun2(2,3)

def fun3(x,y,z=0):
    # print("x+y+z=",x+y+z)
    return x+y+z

a = fun3(1,2,3)
print(a)

# # fun3(2,3,3)
# fun3(z=1,x=5,y=5)

# #可变型参数：*参数

# def fun4(*a):
#     print(a)

# fun4(1,"a",True,[1,2,3,4],{"a":1},(1,2))

# # **a，字典型参数
# def fun5(**a):
#     print(a)

# fun5(x=1,y=2,z=3)


# def fun6(a):
#     print("fun6",a)

#     def fun6_1():
#         print("fun6_1",a)
    
#     fun6_1()

# fun6(10)

#函数的调用


