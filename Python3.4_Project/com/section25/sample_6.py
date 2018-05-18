#!/usr/bin/python3

print("====================摄氏温度和华氏温度相互转换====================")
a = int(input('摄氏度转换为华氏温度请按1\n华氏温度转化为摄氏度请按2\n'))
while a != 1 and a != 2:
    a = int(input('你选择不正确，请重新输入。\n摄氏度转换为华氏温度请按1\n华氏温度转换为摄氏度请按2\n'))
if a == 1:
    # 计算华氏温度
    celsius = float(input('输入摄氏温度：'))
    fahrenheit = (celsius * 1.8) + 32
    print('{0:0.1f} 摄氏温度转为华氏温度为 {1:0.1f}'.format(celsius, fahrenheit))
else:
    # 计算摄氏度
    fahrenheit = float(input('输入华氏温度：'))
    celsius = (fahrenheit - 32) / 1.8
    print('{0:0.1f} 华氏温度转为摄氏温度为 {1:0.1f}'.format(fahrenheit, celsius))
