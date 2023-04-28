
from Method import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

my_sender = sys.argv[3]  # 填写发信人的邮箱账号
my_pass = sys.argv[4]  # 发件人邮箱授权码
my_user = sys.argv[5]  # 收件人邮箱账号

def suyunChinck():
    try:
        driver = get_web_driver()
        driver.get("https://yooo.one/user")
        time.sleep(12)
        #验证是否为真人
        driver.find_element('xpath', '//*[@id="challenge-stage"]/div/label/input').click()
        time.sleep(8)
        driver.find_element('xpath', '//*[@id="email"]').send_keys(username)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="password"]').send_keys(password)
        time.sleep(2)
        driver.find_element('xpath', '//*[@id="login_submit"]').click()
        time.sleep(5)
        try:
            #签到
            driver.find_element('xpath', '//*[@id="checkin"]').click()
            time.sleep(2)
        except NoSuchElementException:
            pass
        finally: 
            print('按钮不可点击，已签到？？')
            #获取元素值
            result1 = driver.find_element('xpath', '//*[@id="kt_subheader"]/div/div[2]/a').text
            result = '签到状态：' + result1
            print(result)
            #获取剩余流量
            left1 = driver.find_element('xpath', '//*[@id="kt_content"]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div').text
            left = '流量剩余：' + left1
           
    except:
        pass
    finally:
        driver.quit()
    time.sleep(3)
    topic = '速云签到'
   
    #发送邮件
    ret = mail(topic,result,left,my_sender,my_user,my_pass)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
    return result
if __name__ == '__main__':
    suyunChinck()
