#!/usr/bin/python3

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print("第三个元素为：", list1[2])
list1[2] = 2001
print("更新后的第三个元素为：", list1[2])
print(list1)
del list1[2]
print("删除第三个元素：", list1)