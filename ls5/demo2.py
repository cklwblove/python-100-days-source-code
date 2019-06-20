"""
可变参数函数定义
"""


# 在参数名前面的*表示args是一个可变参数
# 即在调用 add 函数时，可以传入 0 个或多个参数

def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
