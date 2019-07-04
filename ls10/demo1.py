# -*- coding: utf-8 -*-
"""
读写文本文件
注意编码方式
"""


def main():
    f = None
    try:
        f = open('./致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
