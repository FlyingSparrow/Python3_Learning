#!/usr/bin/python3

print("{0}使用递归斐波那契数列{1}".format('=' * 10, '=' * 10))

def recur_fibo(n):
    """递归函数输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))

nterms = int(input('您要输出几项？'))

if nterms <= 0:
    print('输入正数')
else:
    print('斐波那契数列：')
    for i in range(nterms):
        print(recur_fibo(i), end='\t')


