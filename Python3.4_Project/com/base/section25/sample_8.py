#!/usr/bin/python3

print("====================if语句====================")
while True:
    try:
        num = float(input('请输入一个数字：'))
        if num == 0:
            print('输入的数字是零')
        elif num > 0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
    except ValueError:
        print('输入无效，需要输入一个数字')

