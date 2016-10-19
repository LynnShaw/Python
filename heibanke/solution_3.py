#coding:utf-8
#1.使用已有cookies登录
#2.访问网站获得cookies，并将获得的cookies存储
#3.使用指定参数生成cookies，并用这个cookies登陆

import requests
import re

login_data={'username':'LynnShaw','password':'xxxxxxxxx'}
url='http://www.heibanke.com/lesson/crawler_ex02/'
login_url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'

#采用第二种方法访问网站获得cookies
r2=requests.get(login_url)
c2=r2.cookies

login_data['csrfmiddlewaretoken']=c2['csrftoken']
#csrf双提交cookie，在post数据里提交一次，cookie里提交一次
r3=requests.post(login_url,data=login_data,allow_redirects=False,cookies=c2)
c3=r3.cookies

pass_data={'username':'1211','csrfmiddlewaretoken':c3['csrftoken']}
for passwd in range(31):
    print passwd
    pass_data['password']=passwd
    r5=requests.post(url,pass_data,cookies=c3)
    result=re.findall(r'密码错误',r5.text.encode('utf-8'))
    if len(result):
        print result[0].decode('utf-8')
    else:
        print u'正确答案'
        break
