# -*- coding: utf-8 -*-
"""
读取文件
通过 with 关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
"""


def main():
    try:
        with open('./致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')


if __name__ == '__main__':
    main()
