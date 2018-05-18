#!/usr/bin/python3

print("====================获取最大值函数====================")
print(max(1, 2))
print(max('a', 'b'))

# 也可以对列表和元组使用
print(max([1, 2]))
print(max((1, 2)))

# 更多实例
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))

print("============对比任意多个数字的大小===================")
number = int(input('输入需要对比大小数字的个数：'))
print('请输入需要对比的数字：')
number_list = []
for i in range(1, number+1):
    num = int(input('请输入第 {0} 个数字：'.format(i)))
    number_list.append(num)

print('您输入的数字为：'.format(number_list))
print('最大值为：{0}'.format(max(number_list)))