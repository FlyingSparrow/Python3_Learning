#!/usr/bin/python3

def is_armstrong_number(number):
    # 初始化变量 temp_sum
    temp_sum = 0
    # 指数
    n = len(str(number))
    temp = number
    while temp > 0:
        digit = temp % 10
        temp_sum += digit ** n
        temp //= 10
    if number == temp_sum:
        return True
    else:
        return False

print("{0}阿姆斯特朗数{1}".format('='*10, '='*10))
num = int(input('请输入一个数字：'))

if is_armstrong_number(num):
    print('{0} 是阿姆斯特朗数'.format(num))
else:
    print('{0} 不是阿姆斯特朗数'.format(num))


print("{0}获取指定区间内的阿姆斯特朗数{1}".format('='*10, '='*10))
lower = int(input('最小值：'))
upper = int(input('最大值：'))

for i in range(lower, upper+1):
    if is_armstrong_number(i):
        print(i, end='\t')
