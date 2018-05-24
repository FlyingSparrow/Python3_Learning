#!/usr/bin/python3

print("{0}文件 IO{1}".format('=' * 10, '=' * 10))


with open('test.txt', 'wt') as out_file:
    out_file.write('该文本会写入到文件中\n看到我了吧！')
print('写入文件结束')
print()

print('读取文件，文件内容如下：')
with open('test.txt', 'rt') as in_file:
    text = in_file.read()

print(text)


