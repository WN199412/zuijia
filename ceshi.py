# import time
# import datetime
#
# from django.http import request
#
# order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-7:]
# date = datetime.datetime.now()

import smtplib
from email.mime.text import MIMEText

# 服务器
SMTPServer = "smtp.qq.com"
# 发送邮件的邮箱地址
sender = "1099816374@qq.com"
# 授权密码
passwd = "cxipzfxrnonihcaf"

# 发送的内容
messasge = 'nihao'
# 转为邮件文本
msg = MIMEText(messasge)
# 邮件主题
msg["Subject"] = "你猜猜"
# 邮件的发送者
msg["From"] = sender

# 链接smtp服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
# 登陆
mailServer.login(sender, passwd)
# 发送邮件
mailServer.sendmail(sender, ['c786737525@163.com'], msg.as_string())
