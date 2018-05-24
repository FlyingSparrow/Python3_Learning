#!/usr/bin/python3

import math

print("====================质数判断====================")
num = int(input('请输入一个数字：'))

# 质数大于 1
if num > 1:
    # 查看因子
    square_num = math.floor(num ** 0.5)
    for i in range(2, (square_num+1)):
        if (num % i) == 0:
            print(num, "是合数")
            print(i, "乘以", num//i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或者等于 1，不是质数
else:
    print(num, "不是质数")