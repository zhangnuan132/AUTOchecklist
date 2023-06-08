# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib



# SMTP 邮箱信息
mail_host = "smtp.gmail.com"
mail_username = "huajiaotest"
mail_password = "wreojmjfbphbmkqb"
#pehmrxmudonusqni
mail_sender = "huajiaotest"

# 发邮件
def send_mail(mail_title="自动化 checklist",   # 邮件标题
              mail_info='<p> 下面是xx号自动化执行链接，点击即可'
                        '<a href="http://localhost:63342/AUTOchecklist/pytest_demo/report/2023.02.27_21:02:56/html/index.html?_ijt=p2hu9m8omtr9esb2c5129daqo7#behaviors/d5e2eb8f48666866056348ababb3e0b1/9d2d9c7bb636425c/">自动化</a>'
                        '    今日newdev打包邮件（64位瘦身渠道包）...</p><p>统计图(见附件)：</p><p><img src="cid:imgid"></p>',   # 邮件内容
              mail_receivers="zhangchenchen-hj@huafang.com",   # 收件人列表
              mail_encode="utf-8",      # 编码
              mail_sender_show_name="checklist回归"):      # 发件人展示名称

    # TODO
    msgAlternative = MIMEMultipart('alternative')
    message = MIMEMultipart('related')

    message['Subject'] = Header(mail_title, mail_encode)
    message['From'] = Header(mail_sender_show_name, mail_encode)
    message['To'] = Header('g-huajiao-qa', mail_encode)
    # message['Subject'] = mail_title

    msg_text = MIMEText(mail_info, 'html', mail_encode)
    message.attach(msg_text)

    # TODO
    # fp = open('pic.png','rb')
    # print(type(fp))
    # # fp = open('pic.png',encoding="UTF-8")
    # img_data = fp.read()
    # msg_image = MIMEImage(img_data)
    # # msg_image.add_header('Content-ID', '<imgid>')
    # message.attach(msg_image)

    msgAlternative.attach(MIMEText(mail_info, 'html', 'utf-8'))

    smtp_obj = smtplib.SMTP_SSL(mail_host, 465)



    # smtpObj = smtplib.SMTP()
    # smtpObj.connect(mail_host, 25)

    # address = open('address.txt')
    # emails = address.readlines()
    # emails1 = []
    # # print('email = ', emails)
    # for i in emails:
    #     emails1.append(i.strip('\n'))
    # print('email1 = ', emails1)
    # for i in emails1:
    #     mail_receivers = mail_receivers + i + ','
    #
    # print('mail_receivers = ',mail_receivers)
    try:
        smtp_obj.login(mail_username, mail_password)
        try:
            smtp_obj.sendmail(mail_sender, mail_receivers.split(','), message.as_string())
            print("邮件发送成功")
        except Exception as e:
            print("邮件发送失败！")
    except Exception as e:
        print("邮件服务器链接失败！")




if __name__ == '__main__':
    send_mail()

