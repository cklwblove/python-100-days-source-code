"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示 大一点/小一点/猜对了

Version: 0.0.1
Author: lwb
"""

import random

answer = random.randint(1, 100)
counter = 0

while True:
    counter += 1
    number = int(input('请输入： '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        # break 终止本次循环
        break

print('你总共猜对了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
