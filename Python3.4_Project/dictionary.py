#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8
dict['School'] = "菜鸟教程"

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name'] # 删除键
dict.clear()      # 清空字典
del dict          # 删除字典

