#!/usr/bin/python3

print("================类示例====================")
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self):
        self.data = []
    def f(self):
        return 'hello world'

x = MyClass()

print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
print("====================================")

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)
print("====================================")

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
print("====================================")

print("================类的继承示例====================")
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d 岁。"%(self.name, self.age))

# 单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级"%(self.name, self.age, self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name, self.topic))

# 多重继承示例
class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

p = people('runoob', 10, 30)
p.speak()

s = student('ken', 10, 60, 3)
s.speak()

test = sample("Tim", 25, 80, 4, "Python")
test.speak()

print("================方法重写示例====================")
class Parent:
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):
    def myMethod(self):
        print('调用子类方法')

c = Child()
c.myMethod()
super(Child, c).myMethod()

print("================类属性与方法示例====================")
class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print("====================================")

class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name: ', self.name)
        print('url: ', self.__url)

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()
x.foo()

print("================运算符重载示例====================")
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)'%(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)