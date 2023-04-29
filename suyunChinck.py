
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
        driver.get("https://yooo.one/auth/login")
        time.sleep(12)
        print('#验证是否为真人')
        try:
            driver.find_element('xpath', '//*[@id="challenge-stage"]/div/label/input').click()
            time.sleep(6)
        except:
            print('cf人机验证未找到点击元素')
        print('#开始登录')
        print(driver.page_source)
        print(driver.current_url)
        driver.find_element('xpath', '//*[@id="email"]').send_keys(username)
        time.sleep(2) 
        driver.find_element('xpath', '//*[@id="password"]').send_keys(password)
        time.sleep(2)    
        driver.find_element('xpath', '//*[@id="login_submit"]').click()
        time.sleep(5)
        print('开始签到')
        try:
            #签到
            driver.find_element('xpath', '//*[@id="checkin"]').click()
            time.sleep(2)
        except:
            print('签到元素不可用')
        finally: 
            #获取元素值
            result1 = driver.find_element('xpath', '//*[@id="kt_subheader"]/div/div[2]/a').text
            result = '签到状态：' + result1
            print(result)
            #获取剩余流量
            left1 = driver.find_element('xpath', '//*[@id="kt_content"]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div').text
            left = '流量剩余：' + left1
           
    except:
        print('整个过程失败')
    finally:
        driver.quit()
    time.sleep(1)
    topic = '速云签到'
   
    #发送邮件
#     ret = mail(topic,result,left,my_sender,my_user,my_pass)
#     if ret:
#         print("邮件发送成功")
#     else:
#         print("邮件发送失败")
    return 
if __name__ == '__main__':
    suyunChinck()
