# -*- coding: utf-8 -*-
"""
网络编程
发送电子邮件
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'lwbhtml@163.com'
    receivers = ['liwb@hundsun.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('liwb', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成！')


if __name__ == '__main__':
    main()
