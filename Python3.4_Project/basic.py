#!/usr/bin/python3

import sys
from sys import argv,path

str = 'Runoob'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+'你好')

print('--------------------------')

print('hello\nrunoob')
print(r'hello\nrunoob')

x = "a"
y = "b"

print(x)
print(y)

print('------------------------')
print(x, end=" ")
print(y, end=" ")
print()

print('===============Python import mode=========================');
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)

print('================python from import=========================')
print('path: ', path)