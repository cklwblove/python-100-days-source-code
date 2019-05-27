"""
多行注释
使用变量保存数据并进行算术运算

Author: liwb
Version: 0.0.1
"""
a = 321
b = 123

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or \
           year % 400 == 0


print(is_leap(2005))

keys = ['1001', '1002', '1003']
values = ['骆昊', '王大锤', '白元芳']
d = dict(zip(keys, values))
print(d)
