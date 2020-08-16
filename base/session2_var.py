'''
类型 变量名=value
python 变量名=value
id() - 获取对象的内存地址
type() - 获取对象的类型
'''

a = 1
print(id(a),type(a),a)

a = "str"  
#print(id(a),type(a),a)

b = 1
#print(id(b),type(b),a)


a = True
a = []
print(id(a))
a.append(2)
print(id(a[0]))



a = ()
a = {}