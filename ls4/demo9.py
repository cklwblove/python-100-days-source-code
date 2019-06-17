"""
寻找水仙花数

Version: 0.0.1
Author: liwb
"""

max_num = int(input('请输入最大范围：'))

for num in range(0, max_num):

    length = len(str(num))

    count = length

    num_sum = 0

    while count:
        num_sum += int((str(num)[count - 1])) ** length
        count -= 1
    else:
        if num_sum == num:
            print('%d is a %d bit narcissistic_number' % (num, length))
        else:
            print('%d is not a narcissistic_number' % num)
