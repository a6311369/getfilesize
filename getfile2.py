#coding=utf-8
import os
import os.path
import math
import smtplib
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from getpass import getpass

list1 = []
b = []
path2 = []


def get_size(path):
    fileList = os.listdir(i)  # 獲取path目錄下所有文件
    # fileList = os.listdir(path)  # 獲取path目錄下所有文件
    for filename in fileList:
        pathTmp = os.path.join(path, filename)  # 獲取path與filename組合後的路徑
        if os.path.isdir(pathTmp):  # 判斷是否為目錄
            get_size(pathTmp)  # 是目錄就繼續遞迴尋找
        elif os.path.isfile(pathTmp):  # 判斷是否為檔案
            filesize9 = os.path.getsize(pathTmp)  # 如果是檔案，則獲取相應檔案的大小
            filesize = filesize3(os.path.getsize(pathTmp))  # 如果是檔案，則獲取相應檔案的大小
            if filesize9 > 536870912:  # 檔案大小比對，超過500MB就抓出來
                a = '該檔案超過500MB', '檔案名稱：%s' % filename, '檔案大小：%s' % filesize,'檔案路徑 : %s' %pathTmp
                c = print(a)
                b.append(c)  # 將檔案名稱增加到list內
                b.remove(None)

# 位元組轉換
def roundstr(size):
    return str(round(size, 1))  # round(size, 1) 取小數第一位後開始四捨五入


def filesize3(bytesize):
    if bytesize < 1024:
        return str(bytesize) + ' Bytes'
    elif bytesize < 1024 ** 2:  # **為返回x的y次方
        return roundstr(bytesize / 1024.0) + ' KBytes'
    elif bytesize < 1024 ** 3:
        return roundstr(bytesize / (1024.0 ** 2)) + ' MBytes'
    elif bytesize < 1024 ** 4:
        return roundstr(bytesize / (1024.0 ** 3)) + ' GBytes'
    elif bytesize < 1024 ** 5:
        return roundstr(bytesize / (1024.0 ** 4)) + ' TBytes'
    else:
        return str(bytesize) + ' Bytes'


# path = 'C:\\影片\\無聊詹'    #指定路徑
# 讀取檔案開始
f = open('C:\\path.txt', 'r')
ff = f.readline().split(',')  # 利用split功能取逗號為切斷點
for i in ff:
    get_size(i)
print(b)
f.close()

# #send email
# OUTLOOK_USER = input("Enter your Outlook email: ")   #輸入outlook帳號
# OUTLOOK_PWD = getpass("Enter password: ")            #輸入outlook密碼
#
# SUBJECT = 'Test Email' #mail主旨
# BODY = str(b)          #mail 內文
# TO = 'xxx@gmail.com'   #收件者mail
#
# def sendEmail(sender, pwd, to, subject, message):
#     recipient = to if type(to) is list else [to]
#     msg = MIMEText(message)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = COMMASPACE.join(recipient)
#     server = smtplib.SMTP('smtp.live.com:587')  #hotmail的smtp server
#     server.ehlo()
#     server.starttls()
#
#     try:
#         server.login(sender,pwd)
#         print('Successfully authenticated...')
#     except smtplib.SMTPAuthenticationError:               # Check for authentication error
#         return " Authentication ERROR"
#
#     try:
#         server.sendmail(sender,recipient,msg.as_string())
#         print('Email sent!')
#     except smtplib.SMTPRecipientsRefused:                # Check if recipient's email was accepted by the server
#         return "ERROR"
#     server.quit()
#
# sendEmail(OUTLOOK_USER, OUTLOOK_PWD, TO, SUBJECT, BODY)
