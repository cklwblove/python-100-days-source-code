# -*- coding: utf-8 -*-
"""
从一段文字中提取国内手机号码

国内三家运营商
电信号段：133/153/180/181/189/177
联通号段：130/131/132/155/156/185/186/145/176
移动号段：134/135/136/137/138/139/150/151/152/157/158/159/182/183/184/187/188/147/178
"""
import re


def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('---------华丽的分割线-------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------华丽的分割线---------')
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
