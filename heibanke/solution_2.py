#coding:utf-8
import scrapy
__author__ = 'xiaoningning'

import requests
import re

form_data={
   # 'csrfmiddlewaretoken':'pCOHKhN4vpyvkQFwz8LiUK4bFi4ncAqm',
    'username':1211,
}
url='http://www.heibanke.com/lesson/crawler_ex01/'
for password in range(1,31):
    form_data['password']=password
    r = requests.post(url, data=form_data)
    #print r.text
    print form_data
    result=re.findall(r'密码错误',r.text.encode('utf-8'))
    if len(result):
        print result[0].decode('utf-8')
    if not result or password>30:
        print r.text
        break


