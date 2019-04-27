#!/usr/bin/python3

import random

print("====================随机数====================")
# 随机数字小游戏
i = 1
a = random.randint(0, 100)
b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
while a != b:
    if a > b:
        print('你第 {0} 次输入的数字小于电脑随机数字'.format(i))
        b = int(input('请再次输入数字:'))
    else:
        print('你第 {0} 次输入的数字大于电脑随机数字'.format(i))
        b = int(input('请再次输入数字:'))
    i += 1
else:
    print('恭喜你，你第 {0} 次输入的数字与电脑的随机数字 {1} 一样'.format(i, b))
