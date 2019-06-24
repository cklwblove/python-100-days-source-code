"""
和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或将列表中的一部分取出来创建新的列表
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通过反向切片来操作获取倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
