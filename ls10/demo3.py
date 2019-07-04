# -*- coding: utf-8 -*-

"""
读取文件
使用文件对象的 read 方法读取文件
使用 for-in 循环逐行读取或者用 readlines 方法将文件按行读取到一个列表容器中
"""

import time


def main():
    # 一次性读取整个文件内容
    with open('./致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过 for-in 循环读取
    with open('./致橡树.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('./致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
