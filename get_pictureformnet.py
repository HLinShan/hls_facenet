#coding = utf-8
# 从百度下载图片，输入关键字，下载到本地，模拟人工点击
import time
from selenium import webdriver
import os
import requests
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request
import lxml
import lxml.html
import numpy
import time
import re
# 定义下载函数
def download(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        print("download ok ")
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        print("download no ok ")
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

def url_open(url):
    res = request.Request(url)
    res.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
    html = request.urlopen(res, timeout=60).read()
    return html

# 隐式打开一个浏览器
def open_Explor():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver






path_list=[u'邓紫棋' ,u'关晓彤' ,u'焦俊艳' ,u'杨颖' ,u'刘诗诗' ,u'倪妮' ,
           u'刘涛' ,u'乔振宇' ,u'易烊千玺' ,u'杨祐宁' ,u'华晨宇' ,u'鹿晗' ,u'周杰伦' ,u'霍建华' ,u'朱一龙' ,u'张晨光' ,u'周星驰' ,
           u'朴有天' ,u'白宇' ,u'吴亦凡' ]

# path_list=[u'西班牙圣家族大教堂',u'日本金阁寺' ]
# path_list=[u'菲律宾共和国国旗',u'印度国旗',u'巴西国旗',u'柬埔寨国旗',u'缅甸国旗'
#     , u'泰国国旗',u'马来西亚国旗',u'新加坡国旗',u'阿富汗国旗',u'伊拉克国旗',u'伊朗国旗',u'叙利亚国旗',u'老挝国旗']
for path_idx in range(len(path_list)):
    path=path_list[path_idx]
    path_dir=u'ls_人脸识别测试'+'/'+path
    print(path+"is begining ___")
    if os.path.exists(path_dir) is False:
        os.makedirs(path_dir)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(8)  # 设置隐式等待时间
    url="https://image.baidu.com/"
    driver.get(url)  # 地址栏里输入网址
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys(path)  # 搜索框输入关键字
    driver.find_element_by_xpath('//*[@class="s_search"]').click()  # 点击百度一下按钮

    print("click  is ok ")
    time.sleep(2)  # 等待2秒


    try:
        hre = driver.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[10]/div/a')
    except:
        hre = driver.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[10]/div/div[1]/a')
    next_url=hre.get_attribute("href")
    driver.get(next_url)

    # 设置下载的图片数量及进行下载
    start = 1
    end = 30
    i=0
    # for i in range(start,end + 1):
    #     # 获取图片位置
    # img = driver.find_elements_by_xpath(xpath)
    print("333")
    for num in range(start,end+1):
        html=driver.page_source
        a=re.findall(r'src="([^<]+?\.jpg)',html)
        print(a)
        try:
            if 'jpg' in a[0]:
                url=a[0].replace("amp;",'')
                print("url",url)
                img_name = url.split('/')[-1]
                filename = os.path.join(path_dir, img_name[-25:])
                download(url,filename)
                # print(num + 1, "存入成功")
            else:
                print(num + 1, "存入失败")
            driver.find_element_by_xpath('//*[@id="container"]/span[2]').click()  # 翻到下一页
            print("完成！")
            time.sleep(3)
            print(path+'%d/%d'%(num,end))
        except Exception:
            print("this is some bug")
            pass

    driver.quit()





# for ele in img:
#         #   获取图片链接
#     target_url = ele.get_attribute("src")
#     print(target_url)
#         #   设置图片名称。以图片链接中的名字为基础选取最后25个字节为图片名称。
#     img_name = target_url.split('/')[-1]
#     filename = os.path.join(path, img_name[-25:])
#     if "jpg" in filename:
#         download(target_url, filename)
# #     # 下一页
# #     next_page = driver.find_element_by_class_name("img-next").click()
#     time.sleep(3)
# #     # 显示进度
#     i=i+1
#     print('%d / %d' % (i, len(img)))

# 关闭浏览器








