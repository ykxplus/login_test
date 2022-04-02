from bs4 import BeautifulSoup

html='''
<meta charset="UTF-8"> <!-- for HTML5 -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<html><head><title>yoyo ketang</title></head>
<body>
<b><!--Hey, this in comment!--></b>
<p class="title"><b>yoyoketang</b></p>
<p class="yoyo">这里是我的微信公众号：yoyoketang
<a href="http://www.cnblogs.com/yoyoketang/tag/fiddler/" class="sister" id="link1">fiddler</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/python/" class="sister" id="link2">python</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/selenium/" class="sister" id="link3">selenium</a>;
快来关注吧！</p>
'''

#获取title对象
soup=BeautifulSoup(html,'html.parser')
print(soup.title)

#获取title的标签名称
print(soup.title.string)

#获取title的值
print(soup.find_all("title"))

#获取第一个p标签对应id的值
print(soup.p["class"])

print(soup.find_all("a"))

for s in soup.find_all("a"):
    print(s['href'])
    # print("href={}".format(s['href']))