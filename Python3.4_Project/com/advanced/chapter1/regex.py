#!/usr/bin/python3

import re

print("{0}正则表达式{1}".format('=' * 10, '=' * 10))
# 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())
# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))

print("{0}".format('=' * 30))
line = 'Cats are smarter than dogs'
