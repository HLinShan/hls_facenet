#coding = utf-8
from urllib import request
from  bs4 import BeautifulSoup
import lxml
import re
import time
import os
import socket



path="image"
if not os.path.exists(path):
    os.mkdir(path)
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
url = "https://pic.sogou.com/pics?query=%B3%A4%B3%C7&di=2&_asf=pic.sogou.com&w=05009900&sut=9609&sst0=1553487449809"
# https://www.quanjing.com/category/110481.html
html = request.urlopen(url).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

# 用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
links = soup.find_all('img')
# print("links",links)
print("=========")

# 设置保存图片的路径，否则会保存到程序当前路径
i=0
for link in links:
    # print(link)
    img_scr=link.get('src')
    print(img_scr)
    if img_scr :

        if 'http' in img_scr:


            try:
                print(path + '/%s.jpg' % i)
                request.urlretrieve(img_scr, path + '/%s.jpg' % i)
                print('Downloading %s picture now!!!' % i)
                i=i+1
            except Exception as e:
                pass

    # 保存链接并命名，time.time()返回当前时间戳防止命名冲突
    #         request.urlretrieve(link.arr, path + '/%s.jpg' % time.time())  # 使用request.urlretrieve直接将所有远程链接数据下载到本地

