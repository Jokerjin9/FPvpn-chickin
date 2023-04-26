import requests
import time
from bs4 import BeautifulSoup
from lxml import etree
from Method import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

my_sender = sys.argv[3]  # 填写发信人的邮箱账号
my_pass = sys.argv[4]  # 发件人邮箱授权码
my_user = sys.argv[5]  # 收件人邮箱账号

def sjs():
    header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    ajax_header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }
    date = {
      "username":username,
      "password":password

    }
    chepiao = 'https://sjsss.vip/home.php?mod=space&uid=174999'
    recat_url = 'https://sjsss.vip/k_misign-sign.html'
    chick_url = 'https://xsijishe.net/plugin.php?id=k_misign:sign&operation=qiandao&formhash=a63ffbfd&format=empty'
    login_url = 'https://xsijishe.net/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=Lx8kI&inajax=1'
    s = requests.Session()
    r = s.post(url=login_url,headers=header,data= date)
    # 获取登录成功后的cookie信息
    cookiejar = r.cookies
    # 把cookie转换成字典
    cookies = requests.utils.dict_from_cookiejar(cookiejar)

    time.sleep(3)
    print('开始签到')
    try:
        chick = s.get(chick_url,headers=ajax_header,cookies =cookies)
        print(chick.status_code)

    except:
        pass
    # 确认状态
    recat = s.get(recat_url,headers=header,cookies=cookies)
    soup = BeautifulSoup(recat.text, 'html.parser') # 解析网页内容
    dom = etree.HTML(str(soup))
    result = dom.xpath('//*[@id="wp"]/div[2]/div[1]/div[1]/div/div[1]')[0].text
    #查看车票
    cp = s.get(chepiao,headers=header,cookies = cookies)
    soupcp = BeautifulSoup(cp.text, 'html.parser') # 解析网页内容
    domcp = etree.HTML(str(soupcp))
    left = domcp.xpath('//*[@id="psts"]/ul/li[4]/text()')
    #发送邮件
    ret = mail(result,left,my_sender,my_user,my_pass)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
    return result


if __name__ == '__main__':
        sjs()
