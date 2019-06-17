"""
摇色子

Version: 0.0.1
Author: liwb
"""

from random import randint


def roll_dice(n=2):
    """
    摇色子
    :param n: 色子的个数
    :return: n颗色子点数之和
    """

    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))