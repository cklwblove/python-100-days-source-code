"""
实现判断一个数是不是素数

Version: 0.0.1
Author: liwb
"""

def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False