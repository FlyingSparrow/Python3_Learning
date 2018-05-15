#!/usr/bin/python3

tup1 = ()
tup1 = (50)
print(type(tup1))

tup1 = (50,)
print(type(tup1))

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]", tup2[1:5])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 创建一个新的元组
tup3 = tup1 + tup2;
print(tup3)