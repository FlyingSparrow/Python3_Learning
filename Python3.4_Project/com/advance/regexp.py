#!/usr/bin/python3
import re


line = "Cats are smarter than dogs"

print('match demo')
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2): ", matchObj.group(2))
else:
    print("No match!!")


print()
print('search demo')
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print("searchObj.group(): ", searchObj.group())
    print("searchObj.group(1): ", searchObj.group(1))
    print("searchObj.group(2): ", searchObj.group(2))
else:
    print("Nothing found!!")


print()
print()
print('the different between match() and search()')
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group(): ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print("search --> matchObj.group(): ", matchObj.group())
else:
    print("No match!!")


print()
print()
print('find and replace')

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话好莫啊：", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码：", num)


# 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
























