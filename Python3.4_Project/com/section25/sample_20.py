#!/usr/bin/python3

print("{0}ASCII码与字符相互转换{1}".format('='*10, '='*10))
# 用户输入字符
c = input('请输入一个字符：')

# 用户输入 ASCII 码，并将输入的数字转为整型
a = int(input('请输入一个ASCII码：'))

print('{0} 的ASCII码为 {1}'.format(c, ord(c)))
print('{0} 对应的字符为 {1}'.format(a, chr(a)))