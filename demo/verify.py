#coding=utf-8
import requests
import time
import sys, io

headers_1 = {
'Host': 'so.gushiwen.org',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

headers_2 = {
'Host': 'so.gushiwen.org',
'Connection': 'keep-alive',
'Content-Length': '303',
'Cache-Control': 'max-age=0',
'Origin': 'http://so.gushiwen.org',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

sess = requests.session()

sess.get('http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx', headers=headers_1)

response = sess.get("http://so.gushiwen.org/RandCode.ashx",headers=headers_1)


with open('code.png','wb')as f:
    f.write(response.content)

code = input('请输入验证码:')

form_data = {
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'denglu': '登录',
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    '__VIEWSTATE': 'H2dbNnLxIFAytzlqfQc1JTJLadgzdNdE7uOdVx4nPkPZ28kzi2R4Ewgzo/2enNmQ0uYSlQ6Bvv3bG8Z3gegDwkmqSMe+xzaJY8W27FJMwijwYgk4T0tHJFsR4KE=',
    'code': code,
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'pwd': '123456',
    'email': '1030153984@qq.com',
}



response = sess.post("http://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx",data=form_data,headers=headers_2)

print(sys.stdout.encoding)

# print(response.                                                                                                                                                                                                                   ext)
with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

