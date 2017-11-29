from selenium import webdriver
import requests
from PIL import ImageGrab
from PIL import Image
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
#设置等待时间，因为可能要经常使用，就赋值变量
wait = WebDriverWait(browser,10)
def search():
    #可能会因为网络的原因报时间等待的异常，使用t异常处理
    try:
        browser.get('https://www.iqianjin.com/user/register')
        input = wait.until(#获取手机输入文本框
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mobile'))
        )
        password = wait.until(  # 获取密码的框
            EC.presence_of_element_located((By.CSS_SELECTOR, '#rpassword'))
        )
        for num in range(13000000000,13999999999,1):
            input.send_keys(num)#用于注册手机的填写
            password.send_keys('11')  # 用于注册手机的填写
            time.sleep(0.1)
            try:
                # 获取验证
                verify = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#registerForm > fieldset > div:nth-child(2) > label.error')))
                # verify = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#registerForm > fieldset > div:nth-child(2) > label.error.valid')))
                print(verify.text)
                if verify.text == "该手机号存在，是您本人可立即登录":
                    with open('number.txt','a') as f:
                        f.write(str(num) + '\n')
            except NoSuchElementException:
                return 100
            finally:
                input.clear()
                password.clear()

        # return 50
    except TimeoutException:
        return search()
def main():
    total = search()
    print(total)


if __name__ == '__main__':
    main()

