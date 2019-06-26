"""
使用字典
可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是有一个键和一个值组成的键值对
"""


def main():
    scores = {'liwb': 95, 'byf': 78, 'drj': 82}
    # 通过键可以获取字典对应的值
    print(scores['liwb'])
    print(scores['byf'])
    print(scores['drj'])
    # 循环
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新
    scores['byf'] = 65
    scores['zgwl'] = 71
    scores.update(冷面=67, 方齐禾=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get 方法也可以设置默认值
    print(scores.get('武则天'), 60)
    # 删除
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('liwb', 100))
    # 清空
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
