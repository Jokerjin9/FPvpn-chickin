import time

from GoodJob import *

username = sys.argv[1] 
password = sys.argv[2] 

def Chickin():
    driver = get_web_driver()
    driver.get('https://xsijishe.net/k_misign-sign.html')  # 打开签到页面
    time.sleep(8)
    driver.find_element('xpath', '//*[@id="JD_sign"]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="loginform_Lwz0Z"]/div/div[1]').send_keys(username)
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="loginform_Lwz0Z"]/div/div[2]').send_keys(password)
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="loginform_Lwz0Z"]/div/div[6]/button').click()
    time.sleep(5)
    #chickin
    try:
        driver.find_element('xpath', '//*[@id="JD_sign"]').click()
    except:
        pass
    #获取签到状态
    res = driver.find_element('xpath', '//*[@id="JD_sign"]').text
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="wp"]/div[2]/div[1]/div[2]/div/h3/div').click()
    time.sleep(2)
    point = driver.find_element('xpath', '//*[@id="psts"]/ul/li[2]/text()').text
    time.sleep(2)
    print(res,point)
    driver.quit()

if __name__ == '__main__':
        Chickin()
