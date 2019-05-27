"""
使用input函数输入
使用int()进行类型转换
使用占位符格式化输出的字符串

Author: liwb
Version: 0.0.1
"""

a = int(input('a= '))
b = int(input('b= '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
