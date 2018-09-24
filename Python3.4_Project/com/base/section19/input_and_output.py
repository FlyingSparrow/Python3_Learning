#!/usr/bin/python3

import pprint, pickle

print("==============文件写入示例========================")
f = open("D:/tmp/foo.txt", "w")

num = f.write("Python 是一个非常好的语言。\n是的，的确非常好！！！\n")
print(num)

f.close()

print("======================================")
f = open("D:/tmp/foo.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
f.write(s)

f.close()

print("==============文件读取示例========================")
f = open("D:/tmp/foo.txt", "r")

str = f.read()
print(str)

f.close()

print("======================================")
f = open("D:/tmp/foo.txt", "r")

str = f.readlines()
print(str)

f.close()

print("======================================")
f = open("D:/tmp/foo.txt", "r")

for line in f:
    print(line, end="")

f.close()

print("==============pickle示例========================")
# 使用 pickle 模块将数据对象保存到文件中
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)

output.close()

print("======================================")
# 使用 pickle 模块从文件中重构 python 对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()










