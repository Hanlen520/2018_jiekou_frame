#conding=utf-8
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib



from conf.config import get_config
mail_map=get_config()

# import win32com.client as win32
# import warnings
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')
# warnings.filterwarnings('ignore')
#
#
# def sendemail(sub, body):
#     outlook = win32.Dispatch('outlook.application')
#     receivers = ['xxxx@pingan.com.cn;xxxx@pingan.com.cn;xxxx@pingan.com.cn']
#     mail = outlook.CreateItem(0)
#     mail.To = receivers[0]
#     mail.Subject = sub.decode('utf-8')
#     mail.Body = body.decode('utf-8')
#     # 添加附件
#     # mail.Attachments.Add('D:\Users\xxx\Desktop\email.log')
#     mail.Send()
#
#
# sendemail('xxx，xx', 'xxx')

"""
import smtplib
from email.mime.text import MIMEText
email_host = 'smtp.qq.com'     #邮箱地址
email_user = ''  # 发送者账号
email_pwd = ''  # 发送者的密码
maillist ='v-pum@vanke.com'
#收件人邮箱，多个账号的话，用逗号隔开
me = email_user
msg = MIMEText('这是个python测试邮件，不用回复。')    # 邮件内容
msg['Subject'] = 'python测试'    # 邮件主题
msg['From'] = me    # 发送者账号
msg['To'] = maillist    # 接收者账号列表
smtp = smtplib.SMTP_SSL(email_host, 465) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
smtp.sendmail(me, maillist, msg.as_string())
# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('email send success.')
"""

class Send_email(object):
    def __init__(self,testreport):
        self.testreport=testreport

    # 查找最新的测试报告
    @property    #将方法变成属性
    def report(self):
        lists = os.listdir(self.testreport)  # 返回指定文件夹包含的文件或文件夹名字
        lists.sort(key=lambda fn: os.path.getatime(self.testreport + "\\" + fn))  # 用sort()方法重新按时间对目录下的文件进行排序
        filename = os.path.join(self.testreport, lists[-1])  # list[-1]取最新生成的文件或者文件夹
        return filename


    def send_email(self):
        mail_host=mail_map['email_host']
        mail_port=mail_map["email_port"]
        mail_user=mail_map["user"]
        mail_password=mail_map["password"]
        #发送人邮箱名
        mail_sender=mail_map["sender"]
        #收件人
        receivers=["zhangwk02@vanke.com"]

        message=MIMEMultipart()

        f=open(self.report,'rb')
        mail_body=f.read()
        #带附件发送邮箱
        att=MIMEText(mail_body,"base64","utf-8")
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="report.html"'
        message.attach(att)
        f.close()

        msg=MIMEText(mail_body,"html","utf-8")
        message.attach(msg)
        #message = MIMEText(mail_body, _subtype="html", _charset='utf-8')
        message['From']=mail_sender
        message['TO']=",".join(receivers)
        message["Subject"]=Header("接口自动化测试报告","utf-8")
        smtp=smtplib.SMTP_SSL(mail_host,int(mail_port))
        #smtp.starttls()
        #smtp.connect("Outlook.com",587)

        smtp.login(mail_user,mail_password)
        smtp.sendmail(mail_sender, receivers, message.as_string())
        smtp.quit()
        smtp.close()

