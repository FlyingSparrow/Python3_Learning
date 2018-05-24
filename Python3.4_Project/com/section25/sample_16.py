#!/usr/bin/python3

print("{0}九九乘法表{1}".format('='*10, '='*10))
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}'.format(i, j, i*j), end='\t')
    print()


