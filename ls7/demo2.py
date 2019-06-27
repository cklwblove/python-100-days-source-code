# -*- coding: utf-8 -*-

"""
访问可见性问题

属性和方法的访问权限只有两种，就是公开和私有
私有：属性命名添加两个下划线__
"""


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
