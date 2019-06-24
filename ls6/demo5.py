"""
列表的生产式语法创建列表
"""
import sys


def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器，需要耗费多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    # 查看对象占用的内存的字节数
    print(sys.getsizeof(f))
    print(f)


if __name__ == '__main__':
    main()
