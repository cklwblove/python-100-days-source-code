def main():
    str = 'hello world'

    print(len(str))
    # 首字母大写
    print(str.capitalize())
    # 全部大写
    print(str.upper())
    # 从字符串中查找子串所在位置
    print(str.find('or'))
    print(str.find('shit'))
    # print(str.index('or'))
    # print(str.index('shit'))
    print(str.startswith('He'))
    print(str.startswith('hel'))
    print(str.endswith('ld'))
    print(str.center(50, '*'))
    print(str.rjust(50, ' '))
    str1 = 'abc123456'
    print(str1[2])
    print(str1[2:5])
    print(str1[2:])
    print(str1[2::2])
    print(str1[::2])
    print(str1[::-1])
    print(str1[-3:-1])
    print(str1.isdigit())
    print(str1.isalpha())
    # 检测字符串是否以数字和字符构成
    print(str1.isalnum())
    str2 = '  jackfrued@126.com '
    print(str2)
    # 获取字符串修剪左右两侧空格的拷贝
    print(str2.strip())


if __name__ == '__main__':
    main()
