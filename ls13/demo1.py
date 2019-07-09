# -*- coding: utf-8 -*-
"""
网络编程
"""
from time import time
from threading import Thread

import requests


# 继承Thread类创建自定义的线程类
class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('D:/upload/' + filename, 'wb') as f:
            f.write(resp.content)


# 通过requests模块的get函数获取网络资源
# 下面的代码中使用了天行数据接口提供的网络API
# 要使用该数据接口需要在天行数据的网站上注册
# 然后用自己的Key替换掉下面代码的中APIKey即可
def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=6aad5cd0698a866bb5e6375a251512dd&num=10')
    data_modal = resp.json()
    for mm_dict in data_modal['newslist']:
        url = mm_dict['picUrl']
        print(url)
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()
