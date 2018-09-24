#!/usr/bin/python3

print("{0}最小公倍数算法{1}".format('=' * 10, '=' * 10))

def lcm(x, y):
    # 获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    mul = 1
    while (True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input('输入第一个数字：'))
num2 = int(input('输入第二个数字：'))

print("{}和{}的最小公倍数为{}".format(num1, num2, lcm(num1, num2)))