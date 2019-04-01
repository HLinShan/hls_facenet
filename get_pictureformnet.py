#coding = utf-8

import os
import urllib.request
import re
save_folder="meinv/"
if not os.path.exists(save_folder):
    os.mkdir(save_folder)
url = "https://www.quanjing.com/category/110481.html"
page = urllib.request.urlopen(url)
html = page.read()
print(html)    #python3中只能用print(html) python2中能写print html

#正则匹配
reg = r'lowsrc="(.+?\.jpg)" pic_ext'
imgre = re.compile(reg)
imglist = re.findall(imgre, html.decode('utf-8'))
x = 0
print("start dowload pic")
for imgurl in imglist:
    print(imgurl)
    resp = urllib.request.urlopen(imgurl)
    respHtml = resp.read()
    picFile = open(save_folder+'%s.jpg' % x, "wb")
    picFile.write(respHtml)
    picFile.close()
    x = x+1
print("done")