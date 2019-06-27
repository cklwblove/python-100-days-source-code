# -*- coding: utf-8 -*-
"""
类的定义
"""


class Student(object):
    # __init__ 是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法可以为学生对象绑定 name 和 age 两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字全用小写多个单词用下划线连接
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    stu1 = Student('张三', 32)
    stu1.study('Python程序设计')
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
