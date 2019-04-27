#!/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
width = 4
height = 5
print("width=", width, " height=", height, " area=", area(width, height))
print("=================================")

def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
print("=================================")

print("===============关键词参数示例==================")
printme(str = "菜鸟教程")

print("===============默认参数示例==================")
def printinfo(name, age = 35):
    "打印任何传入的字符串"
    print("名字：", name)
    print("年龄：", age)
    return

printinfo(age = 50, name = "runoob")
print("---------------------------")
printinfo(name="runoob")

print("===============不定长参数示例==================")
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(70, 60, 50)

print("===============匿名函数示例==================")
# 可写函数说明
sum = lambda arg1, arg2: arg1+arg2

# 调用 sum 函数
print("相加后的值为：", sum(10, 20))
print("相加后的值为：", sum(20, 20))

print("===============变量示例==================")
total = 0

def sum(arg1, arg2):
    # 返回两个参数的和
    total = arg1 + arg2
    print("函数内是局部变量：", total)
    return total

sum(10, 20)
print("函数外是全局变量：", total)
print("=================================")

num = 1
def fun1():
    global num
    print(num)
    num = 123
    print(num)

fun1()
print(num)
print("=================================")

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)

outer()

