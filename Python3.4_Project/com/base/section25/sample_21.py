#!/usr/bin/python3

print("{0}最大公约数算法{1}".format('=' * 10, '=' * 10))


def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(smaller, 1, -1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
            break

    return hcf


num1 = int(input('输入第一个数字：'))
num2 = int(input('输入第二个数字：'))

print("{}和{}的最大公约数为{}".format(num1, num2, hcf(num1, num2)))
