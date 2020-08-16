# import session9_module1

# session9_module1.name = "Jobpool"
# session9_module1.fun1()

# import session9_module1 as m1
# m1.fun1()

# from session9_module1 import name
# from session9_module1 import fun1
# name = "new name"
# fun1()

# #dir() - 找出模块中定义的所有名称
# import session9_module1 as m1
# # print(dir(m1))
# m1.fun1()

#__name__ 

#
# import sys
# print(sys.path)

#包 - 管理一系列模块命名空间的文件夹

# import jobpool.base.m1
# jobpool.base.m1.m1_fun1()

from jobpool.session.m2 import  m2_fun2
m2_fun2()