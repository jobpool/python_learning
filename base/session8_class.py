#类的定义

# class MyClass1:
#     x = 100
#     def fun1(self):
#         print(self.x)

# c = MyClass1()
# c.fun1()

# #带有构造函数
# class MyClass2:
#     def __init__(self,x):
#         self.x = x
    
#     def show(self):
#         print(self.x)
    
# c = MyClass2(100)
# c.show()

#继承
#基类
class BasePeople:
    name = ""
    age = 0

    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    def profile(self):
        print("我的名字叫{}，今年{}岁".format(self.name,self.age))

# c = BasePeople("卓谱",18)
# c.profile()

#基类2
class BaseScore:
    math = 0
    chinese = 0
    def __init__(self,m,c):
        self.math = m
        self.chinese = c
    
    def show_score(self):
        print("我的成绩：数学{}，语文{}".format(self.math,self.chinese))

#继承
class Student(BasePeople,BaseScore):
    grade = ""
    def __init__(self, n, a,gr,m,c):
        super().__init__(n, a)
        BaseScore.__init__(self,m,c)
        self.grade = gr
    
    def profile(self):
        print("我的名字叫{}，今年{}岁，我在{}班上学".format(self.name,self.age,self.grade))

c = Student("卓谱",18,"5",98,95)
c.profile()
c.show_score()




