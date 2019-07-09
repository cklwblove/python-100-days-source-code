# -*- coding: utf-8 -*-
"""
发送短信
"""

import urllib.parse
import http.client
import json


def main():
    host = '106.ihuyi.com'
    sms_send_uri = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode(
        {'account': '账号', 'password': '密码', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '接收者的手机号',
         'format': 'json'})
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    # 断开连接
    conn.close()


if __name__ == '__main__':
    main()
