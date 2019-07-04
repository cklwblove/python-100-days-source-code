# -*- coding: utf-8 -*-
"""
访问网络API
"""

import requests
import json


def main():
    resp = requests.get('http://v.juhe.cn/dream/category?key=4571d939290314015b7897bbd25c7288')
    data_modal = json.loads(resp.text)
    for news in data_modal['result']:
        print(news)


if __name__ == '__main__':
    main()
