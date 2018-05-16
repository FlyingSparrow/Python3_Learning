#!/usr/bin/python3

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为：%d" % (n, sum))
print("===============================")

var = 1
while var == 1:
    num = int(input("请输入一个数字："))
    print("你输入的数字是：", num)
    var = var+1

print("Good bye!")
print("===============================")


count = 0
while count < 5:
    print(count, " 小于 5")
    count = count+1
else:
    print(count, " 大于等于 5")
print("===============================")


sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程！")
        break
    print("循环数据 "+site)
else:
    print("没有循环数据！")
print("完成循环！")
print("===============================")

for letter in 'Runoob':
    if letter == 'b':
        break
    print('当前字母为：', letter)

var = 10
while var > 0:
    print('当期变量值为：', var)
    var = var -1
    if var == 5:
        break

print("Good bye!")
print("===============================")

for letter in 'Runoob':
    if letter == 'o':
        continue
    print('当前字母为：', letter)

var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('当期变量值为：', var)

print("Good bye!")
print("===============================")

for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        print(n, ' 是质数')
print("===============================")

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass  块')
    print('当前字母：', letter)
print("Good bye!")
print("===============================")

print("=============99乘法法则示例==================")
i=1
while i<=9:
     #里面一层循环控制每一行中的列数
     j=1
     while j<=i:
          mut =j*i
          print("%d*%d=%d"%(j,i,mut), end="  ")
          j+=1
     print("")
     i+=1