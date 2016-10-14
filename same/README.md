#Python爬虫下载same APP频道图片


- 首先用fiddler抓取same的数据包如下:

![](https://raw.githubusercontent.com/LynnShaw/Python/master/same/fiddler.jpg)

- 得到URL，返回的是json数据：
![](https://raw.githubusercontent.com/LynnShaw/Python/master/same/json.jpg)

- 正则匹配，得到图片URL，下载并保存图片