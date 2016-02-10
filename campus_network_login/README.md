#Python程序实现登陆校园网

###深澜系统
首先用wireshark抓取登入登出时的数据包如下:

登入：
![](https://raw.githubusercontent.com/LynnShaw/Python/master/campus_network_login/login.jpg)

登出：
![](https://raw.githubusercontent.com/LynnShaw/Python/master/campus_network_login/logout.jpg)

用request库提交表单