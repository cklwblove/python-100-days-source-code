"""
判断输入的正整数是不是回文素数
"""
import palindrome as pa
import prime as pr

if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if pa.is_palindrome(num) and pr.is_prime(num):
        print('%d 是回文素数' % num)
    else:
        print('%d 不是回文素数' % num)