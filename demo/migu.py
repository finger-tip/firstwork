from selenium import webdriver
import requests
from PIL import ImageGrab
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
browser = webdriver.Chrome()
#设置等待时间，因为可能要经常使用，就赋值变量
wait = WebDriverWait(browser,10)
def search():
    #可能会因为网络的原因报时间等待的异常，使用t异常处理


    try:
        browser.get('https://passport.migu.cn/portal/user/register/msisdn')
        # 等待这么长时间在响应
        input = wait.until(#获取手机输入文本框
            EC.presence_of_element_located((By.CSS_SELECTOR,'#J_Phone'))
        )
        verify = wait.until(#获取验证码的框
            EC.presence_of_element_located((By.CSS_SELECTOR,'#J_ImgCode'))
        )
        message = wait.until(  # 获取短信的框
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_MsgCode'))
        )
        verifyPhoto = wait.until(  # 获取图片链接
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.bodier.regphone > div > div:nth-child(1) > form > div:nth-child(5) > div > img'))
        )
        verifyPhotoUrl = verifyPhoto.get_attribute('src')
        print (verifyPhotoUrl)
        X = verifyPhoto.location
        print(X)
        print(verifyPhoto.size)
        left = verifyPhoto.location['x']-100
        top = verifyPhoto.location['y']-100
        right = verifyPhoto.location['x'] + verifyPhoto.size['width']-100
        bottom = verifyPhoto.location['y'] + verifyPhoto.size['height']-200

        im = ImageGrab.grab((left, top, right, bottom))
        im.save('code.jpg')


        # im = Image.open('code.jpg')
        # print(im.size)
        # im = im.crop((left, top, right, bottom))
        # print(im)
        # im.save('code.jpg')
        # responseUrl = requests.get(verifyPhotoUrl)#, headers=headers_base



        # with open('code.jpg', 'wb')as f:
        #     f.write(responseUrl.content)
        # input.send_keys('手机')#用于注册手机的填写
        # verify.click()

        # total = EC.presence_of_element_located((By.CSS_SELECTOR,'#bottom_pager > div > span.TV-page-move'))

        return 50
    except TimeoutException:
        return search()
def main():
    total = search()
    print(total)


if __name__ == '__main__':
    main()

