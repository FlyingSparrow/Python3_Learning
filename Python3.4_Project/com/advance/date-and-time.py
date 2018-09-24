#!/usr/bin/python3

import time
import calendar

ticks = time.time()
print("当前时间戳为： ", ticks)

localtime = time.localtime(time.time())
print("本地时间为： ", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为： ", localtime)


print("*****格式化日期*****")
# 格式化成 2016-03-20 11:45:39 形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成 Sat Mar 28 22:24:24 2016 形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


print("获取某月日历")
cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历：")
print(cal)

print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())

yearcal = calendar.calendar(2018,2,1,6)
print(yearcal)