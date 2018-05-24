#!/usr/bin/python3

print("{0}十进制转二进制、八进制、十六进制{1}".format('='*10, '='*10))

# 获取用户输入十进制数
dec = int(input('输入数字：'))

print('十进制数为：{}'.format(dec))
print('转换为二进制为：{}'.format(bin(dec)))
print('转换为八进制为：{}'.format(oct(dec)))
print('转换为十六进制为：{}'.format(hex(dec)))