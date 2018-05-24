#!/usr/bin/python3
import math


# 判断数字是否为素数
def is_prime(number):
    if number > 1:
        square_num = math.floor(number ** 0.5)
        for i in range(2, (square_num + 1)):
            if (number % i) == 0:
                return False
        else:
            return True
    return False


print("{0}输出指定范围内的素数{1}".format('='*10, '='*10))
lower = int(input('输入区间最小值：'))
upper = int(input('输入区间最大值：'))
composite_num = 0
prime_num = 0

for num in range(lower, upper + 1):
    # 素数大于 1
    if is_prime(num):
        prime_num += 1
        print(num, end='\t')
    elif num > 1:
        composite_num += 1

print('')
print('{} 个合数'.format(composite_num))
print('{} 个素数'.format(prime_num))
