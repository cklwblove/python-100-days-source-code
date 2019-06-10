"""
用 for 循环实现1~100之间的偶数求和

Version: 0.0.1
Author: liwb
"""

sum = 0
for x in range(2, 100, 2):
    sum += x
print(sum)
