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

def mail(topic,result,left,my_sender,my_user,my_pass):
    
    ret = True
    try:
        msg = MIMEText(('{} \n {}'.format(result, left)), 'plain', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr(["靖哥哥", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["哎哟，哥哥，嗨你好！", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = topic  # 邮件的主题，也可以说是标题

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



def hejing():
    header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    date = {

            'identity': '1275955680@qq.com',
            'password': 'hejing123456'
    }
    login_url = 'https://www.heywhale.com/api/auth/loginByPassword'
    passage_url = 'https://www.heywhale.com/home/user/level/6451b1d208bd92b2ea5e3b92/level'
    r = requests.Session()
    lg = r.post(login_url,headers=header,data=date)
    print(lg.text)
    # 获取登录成功后的cookie信息
    cookiejar = r.cookies
    # 把cookie转换成字典
    cookies = requests.utils.dict_from_cookiejar(cookiejar)
    # cookies = r.cookies.get_dict()
    print(cookies)
    time.sleep(2)
    passage = r.get(passage_url,headers=header,cookies=cookies)
     #查看情况
    # soup = BeautifulSoup(passage.text, 'html.parser') # 解析网页内容
    # print(soup)
    # dom = etree.HTML(str(soup))
    # b = dom.xpath('//*[@id="app-root"]/div[2]/div/div/div/section/div/div[1]/div/div[3]/div[3]/div[2]/span[2]')
    # jf = b[0]
    # print('目前积分：' + jf )





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
