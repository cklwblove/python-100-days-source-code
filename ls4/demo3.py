"""
用 for 循环实现1~100之间的偶数求和

Version: 0.0.1
Author: lwb
"""

sum = 0
for x in range(1, 100):
    if x % 2 == 0:
        sum += x

print(sum)
