"""
实现计算求最大公约数和最小公倍数的函数

Version: 0.0.1
Author: liwb
"""

# 最大公约数
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

# 最小公倍数
def lcm(x, y):
    return x * y

