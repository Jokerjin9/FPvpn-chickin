# from PIL import Image
# import cv2, ddddocr
import numpy as np
# from retrying import retry
from selenium import webdriver
import selenium
import os, sys, time, requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败



def get_web_driver():
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    driver.implicitly_wait(10)  # 所有的操作都可以最长等待10s
    return driver


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(result,left,my_sender,my_user,my_pass):
    
    ret = True
    try:
        msg = MIMEText(('签到状态：{} \n 剩余流量：{}'.format(result, left)), 'plain', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr(["靖哥哥", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["哎哟，哥哥，嗨你好！", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "极速云签到"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


# ret = mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")





#验证码处理
# import ddddocr

# def Ocr_Captcha(Picture):
#         ocr = ddddocr.DdddOcr(beta=True)

#         with open(Picture, 'rb') as f:
#             image = f.read()

#         res = ocr.classification(image)
#         print( res)
#         return res
# if __name__ == '__main__':
#         Ocr_Captcha()
