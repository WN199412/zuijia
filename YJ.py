'''
准备163邮箱
1、设置
2、POP3/SMTP/IMAP
3、POP3/SMTP服务勾选对号
4、IMAP/SMTP服务勾选对号
5、设置授权密码，注意不要和登陆密码相同
'''
def youjian(mail,text):
    import smtplib
    from email.mime.text import MIMEText

    # 服务器
    SMTPServer = "smtp.qq.com"
    # 发送邮件的邮箱地址
    sender = "1099816374@qq.com"
    # 授权密码
    passwd = "cxipzfxrnonihcaf"

    # 发送的内容
    messasge = text
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
    mailServer.sendmail(sender, [mail], msg.as_string())

