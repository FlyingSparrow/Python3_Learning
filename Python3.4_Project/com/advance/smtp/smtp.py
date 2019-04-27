#!/usr/bin/python3

import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.XX.com"
mail_user = "123@456.com"
mail_pass = "123456"

sender = '123@456.com'
receivers = ['123@456.com']

# print("发送纯文本邮件")
# message = MIMEText('Python 邮件发送测试。。。', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException as e:
#     print(e)
#     print("Error: 无法发送邮件")



# print("发送 HTML 邮件")
# mail_msg = """<p>Python 邮件发送测试。。。</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>"""
# message = MIMEText(mail_msg, 'html', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException as e:
#     print(e)
#     print("Error: 无法发送邮件")


# print("发送带附件的邮件")
# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试。。。', 'plain', 'utf-8'))
#
# # 构造附件1，传送当前目录下的test.txt文件
# att1 = MIMEText(open('/home/sprarrow/github/Python3_Learning/Python3.4_Project/com/advance/smtp/test.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="text.txt"'
# message.attach(att1)
#
# # 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('/home/sprarrow/github/Python3_Learning/Python3.4_Project/com/advance/smtp/runoob.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# message.attach(att2)
#
# try:
#     smtpObj = smtplib.SMTP(mail_host, 25)
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
# except smtplib.SMTPException as e:
#     print(e)
#     print("Error: 无法发送邮件")


print("在 HTML 文本中添加图片")
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')
msgRoot['To'] = Header('测试', 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试。。。</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"/></p>
"""

msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('/home/sprarrow/github/Python3_Learning/Python3.4_Project/com/advance/smtp/autumn.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")