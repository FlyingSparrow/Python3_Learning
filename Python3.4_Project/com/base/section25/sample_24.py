#!/usr/bin/python3

import calendar

print("{0}生成日历{1}".format('=' * 10, '=' * 10))

yy = int(input('输入年份：'))
mm = int(input('输入月份：'))

print(calendar.month(yy, mm))