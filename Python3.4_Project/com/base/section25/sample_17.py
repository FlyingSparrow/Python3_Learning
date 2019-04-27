#!/usr/bin/python3

print("{0}斐波那契数列{1}".format('='*10, '='*10))
nterms = int(input('你需要几项？'))

# 第一项和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 0:
    print('请输入一个正整数')
elif nterms == 1:
    print('斐波那契数列：')
    print(n1)
else:
    print('斐波那契数列：')
    print('{0}{1}{2}'.format(n1, ' ', n2), end=' ')
    while count < nterms:
        nth = n1 + n2
        print(nth, end=' ')
        n1 = n2
        n2 = nth
        count += 1

