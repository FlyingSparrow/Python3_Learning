#!/usr/bin/python3

print("==============变量示例=================")
counter = 100
miles = 1000.0
name = "runoob"

print(counter)
print(miles)
print(name)

print("==============字符串示例=================")
str = 'Runoob'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+"TEST")

print("==============列表示例=================")
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)

print("=============元组示例=================")
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)

print("============集合示例=================")
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)

if('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)    # a 和 b 的差集
print(a | b)    # a 和 b 的并集
print(a & b)    # a 和 b 的交集
print(a ^ b)    # a 和 b 中不同时存在的元素

print("============字典示例=================")
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())