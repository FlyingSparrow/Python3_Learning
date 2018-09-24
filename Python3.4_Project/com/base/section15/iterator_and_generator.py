#!/usr/bin/python3

import sys

print("=============迭代器示例=================")
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")
print()

print("=============生成器示例=================")
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

