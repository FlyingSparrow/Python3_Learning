#!/usr/bin/python3


# 计算阶乘的函数
def factorial(number):
    result = 1
    if number == 0:
        return 1
    elif number > 0:
        for i in range(1, number+1):
            result = result * i
        return result
    else:
        raise ValueError('抱歉，负数没有阶乘')

print("{0}阶乘实例{1}".format('='*10, '='*10))
num = int(input('请输入一个数字：'))
if num < 0:
    print('抱歉，负数没有阶乘')
else:
    print('{0} 的阶乘为 {1}'.format(num, factorial(num)))

