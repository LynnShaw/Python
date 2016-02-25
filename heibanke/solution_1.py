# coding:utf-8
__author__ = 'xiaoningning'
import urllib2
from bs4 import BeautifulSoup
import re
import urlparse

root_url = "http://www.heibanke.com/lesson/crawler_ex00"
# root_url="http://www.baidu.com"

response = urllib2.urlopen(root_url)
html_cont = response.read()
# print html.decode('utf-8').encode('gbk')
soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
link = soup.find_all('h3')
link = link[0].encode('gbk')
print link
num=re.findall(r'\d{2,}',link)
#print num
#new_url=urlparse.urljoin(root_url,num[0])
new_url=root_url+'/'+num[0]
#print new_url
while len(num):
    response = urllib2.urlopen(new_url)
    html_cont = response.read()
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
    link = soup.find_all('h3')
    link = link[0].encode('gbk')
    print link
    num=re.findall(r'\d{2,}',link)
    new_url=root_url+'/'+num[0]