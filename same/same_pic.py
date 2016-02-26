#codinr:utf-8
__author__ = 'xiaoningning'

from urlparse import urlsplit
from os.path import basename
import urllib2
import os
import re
import requests

if not os.path.exists('images'):
    os.mkdir("images")

url='https://v2.same.com/channel/1031310/senses'

#s=requests.session()
num=0
response=requests.get(url,verify=False)
while True:


#    print response.text.encode('GBK', 'ignore');

    next_url=re.findall('"next":"([^\"]*)"',response.text)
    next_url='https://v2.same.com'+''.join(next_url)
    #print next_url
    img_urls=re.findall('"photo":"([^\"]*)"',response.text)

    for img_url in img_urls:
        print img_url
        try:
            num+=1
            print num
            img_data = urllib2.urlopen(img_url).read()
            file_name = basename(urlsplit(img_url)[2])
            output = open('images/' + str(num)+'.jpg', 'wb')
            output.write(img_data)
            output.close()
        except:
            pass

    response=requests.get(next_url,verify=False)
