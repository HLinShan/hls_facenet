#coding = utf-8
import requests
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 输入网址为百度图片下的大图下滑界面。而非直接输入关键词的缩略图界面
# import l
os.environ["webdriver.chrome.driver"]="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# brower=webdriver.Chrome()

# brower=webdriver.Chrome()
# brower.get("https://www.cnblogs.com/cnhkzyy/p/7294119.html")

# # 定义下载函数
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
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

# 创建下载目录
path_list=['jinbendaqiao',
           'jianpuzaiwugeku',
           'miandianyangguangdajinta',
           'yinnipoluofutu',
           'shatewangguodasha',
           'dibaifangchuanjiudian',
           'baxijiduxiang'

           # 'dibaihalifata',
           # 'xilapatenongshenmiao',
           # 'xinigejuyuan',
           # 'shengbidedajiaotang',
           # 'yasuofeiyadajiaotang',
           # 'balilufugong'
           #
           ]
url_list=["https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E9%87%91%E9%97%A8%E5%A4%A7%E6%A1%A5&step_word=&hs=0&pn=8&spn=0&di=181737196960&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=1721545377%2C1844080031&os=3167624492%2C3989885020&simid=0%2C0&adpicid=0&lpn=0&ln=1872&fr=&fmq=1553569878420_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F014e75586f07c4a801219c770fdeea.jpg%401280w_1l_2o_100sh.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bzv55s_z%26e3Bv54_z%26e3BvgAzdH3Fo56hAzdH3FZMTh9MDh9M3Q%3D_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
          "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%9F%AC%E5%9F%94%E5%AF%A8%E5%90%B4%E5%93%A5%E7%AA%9F&step_word=&hs=0&pn=1&spn=0&di=35947038270&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1004314933%2C1555841084&os=3035546280%2C450506803&simid=3478948726%2C304575306&adpicid=0&lpn=0&ln=1995&fr=&fmq=1553569944103_R&fm=detail&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fs10.sinaimg.cn%2Fmw690%2F001Pkpetgy6NHyJREwNb9%26690&fromurl=ippr_z2C%24qAzdH3FAzdH3Fks52_z%26e3Bftgw_z%26e3Bv54_z%26e3BvgAzdH3FfAzdH3Fks52_mn1anccca8adev14_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
          "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=miandianyangguangdajinta&step_word=&hs=0&pn=6&spn=0&di=38857155261&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=859862660%2C1529485590&os=2880056922%2C3084347045&simid=3365734668%2C202155878&adpicid=0&lpn=0&ln=1657&fr=&fmq=1553569961434_R&fm=detail&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic38.huitu.com%2Fres%2F20151022%2F581721_20151022112437755377_1.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bgtrtv_z%26e3Bv54AzdH3F1jpwtsAzdH3Fi7tp7AzdH3Fda8c8addAzdH3F88d9n00ccn00_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
          "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=yinnipoluofutu&step_word=&hs=0&pn=6&spn=0&di=23550542181&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2732416650%2C3155991365&os=2844552892%2C2905128261&simid=4170466224%2C519928324&adpicid=0&lpn=0&ln=1889&fr=&fmq=1553569997241_R&fm=detail&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg165.ph.126.net%2FnMSNbL2VJJK8Zv_ZSDDXqw%3D%3D%2F2255177513407321727.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fks52_z%26e3B8mn_z%26e3Bv54AzdH3F4tff8ncmmmAzdH3Fks52AzdH3FfpwptvAzdH3Fnn9lc0nda88a88b98b9nnAzdH3F&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
          "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%B2%99%E7%89%B9%E7%8E%8B%E5%9B%BD%E5%A4%A7%E5%8E%A6&step_word=&hs=0&pn=5&spn=0&di=207225313350&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=856206893%2C1741004752&os=3188305205%2C3590914959&simid=3494478688%2C557503253&adpicid=0&lpn=0&ln=468&fr=&fmq=1553570046838_R&fm=result&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic.yhouse.com%2Flife%2Fimage%2F20150115%2Flife%2F20150115173358_274.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Byi57fj_z%26e3Bv54AzdH3FvAzdH3FLtuj%3Fs%3Dc%26pyrj%3D8aaaa%26t1%3D8an9b&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
          "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E8%BF%AA%E6%8B%9C%E5%B8%86%E8%88%B9%E9%85%92%E5%BA%97&step_word=&hs=0&pn=3&spn=0&di=118822571340&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=4227610304%2C2576684930&os=2509104948%2C2294064785&simid=4225170748%2C649346681&adpicid=0&lpn=0&ln=1968&fr=&fmq=1553570145803_R&fm=detail&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fm.tuniucdn.com%2Ffilebroker%2Fcdn%2Fsnc%2F04%2F0b%2F040b5e75f585f2e3c2eed79d4a1cd5d0_w800_h400_c1_t0.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bp7gt7_z%26e3Bv54AzdH3F28bab0lnAzdH3Fi5pjsftg2sjri5p5AzdH3F%3Ft1%3D9lmbmc&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",
          "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%B7%B4%E8%A5%BF%E5%9F%BA%E7%9D%A3%E5%83%8F&step_word=&hs=0&pn=6&spn=0&di=22710891830&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1554838716%2C4093511554&os=438089428%2C793978790&simid=3505273069%2C228644779&adpicid=0&lpn=0&ln=1974&fr=&fmq=1553570251629_R&fm=detail&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fgss0.baidu.com%2F9fo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F91529822720e0cf32d8839950e46f21fbe09aa65.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fr5oj6_z%26e3Bkwt17_z%26e3Bv54AzdH3Fq7jfpt5gAzdH3F89lcdncd0d9mdmc98nl_z%26e3Bip4s%3Fjgp6y%3Dqk_k65ofj_1juw7sp&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined",

          ]

# path='shengbidedajiaotang'
# if os.path.exists(path) is False:
#     os.makedirs(path)
#
#
# # 进入百度图片详细查看页
# # url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%8E%89%E6%A1%82%E7%8B%97&step_word=&hs=2&pn=0&spn=0&di=122032263430&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=4287920973%2C3127191504&os=1474905083%2C20535971&simid=3427141834%2C56145588&adpicid=0&lpn=0&ln=1059&fr=&fmq=1540558077513_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fitem%2F201602%2F14%2F20160214211446_izjX4.thumb.700_0.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B17tpwg2_z%26e3Bv54AzdH3Fks52AzdH3F%3Ft1%3Dcnldal90c&gsm=0&rpstart=0&rpnum=0&islist=&querylist='
# # url='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E9%95%BF%E5%9F%8E&step_word=&hs=2&pn=2&spn=0&di=202917329010&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=4251943169%2C3964597261&os=1388253705%2C1971436019&simid=3481966264%2C245486094&adpicid=0&lpn=0&ln=1860&fr=&fmq=1553511539032_R&fm=detail&ic=undefined&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.51wendang.com%2Fpic%2Fc30fbbcc95e1216666fe738b%2F3-810-jpg_6-1080-0-0-1080.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bc8ojg1wg2_z%26e3Bv54AzdH3F15vAzdH3Fvnaukkvvlcj8d8mmmmuj0nbkAzdH3Fn&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
# url="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E9%95%BF%E5%9F%8E&step_word=&hs=2&pn=332&spn=0&di=114950787160&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=3188911405%2C3265111144&os=2890783441%2C3466170543&simid=3340431866%2C118166562&adpicid=0&lpn=0&ln=1860&fr=&fmq=1553511539032_R&fm=detail&ic=undefined&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimage.xcar.com.cn%2Fattachments%2Fa%2Fday_20140307%2F2014030710_56654b16432ddf2109a5Akv2DDHmiToS_sst_560.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fw_z%26e3Bxvw6_z%26e3Bv54_z%26e3BvgAzdH3FkkfAzdH3Fpi6jw1-da8alb0n-a_z%26e3Bip4s%3Fz5gjvstvh%3D8aabad&gsm=14a&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
# url="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E6%95%85%E5%AE%AB&step_word=&hs=2&pn=0&spn=0&di=104630033970&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=729272580%2C3354086757&os=639847590%2C2002525522&simid=4208853657%2C758680559&adpicid=0&lpn=0&ln=1738&fr=&fmq=1553519453788_R&fm=result&ic=undefined&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic.kekenet.com%2F2017%2F0601%2F98041496308248.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bhjhjgjp_z%26e3Bv54AzdH3FA6ptvsjAzdH3Fda80amAzdH3Fc8d80d_z%26e3Bfip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
# url='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%8C%97%E4%BA%AC%E5%A4%A9%E5%9D%9B&step_word=&hs=2&pn=0&spn=0&di=106140716110&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=597649129%2C2475238349&os=4085628137%2C2184679378&simid=4256340604%2C876779383&adpicid=0&lpn=0&ln=1629&fr=&fmq=1553524735753_R&fm=result&ic=undefined&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.lygcct.com%2FUploadFiles%2F2016-01%2F0%2F201601201557347450.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bsy2vvp_z%26e3Bv54AzdH3FIpj4AzdH3FSi5o_z%26e3Bwfr%3F4%3Dc%261%3D0dm&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
# url="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%90%89%E9%9A%86%E5%9D%A1%E5%8F%8C%E5%AD%90%E5%A1%94&step_word=&hs=2&pn=0&spn=0&di=74837155140&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=3506098474%2C644631941&os=3866092314%2C1362190196&simid=3418543903%2C265281858&adpicid=0&lpn=0&ln=1713&fr=&fmq=1553564517193_R&fm=detail&ic=undefined&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.byecity.com.cn%2Ffs%2Fbrs%2Fimgs%2Fmenpiao%2F2015-04%2Fshuangzita7.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bkwtvijg2_z%26e3Bv54AzdH3F3tjf5g23tAzdH3Fftg2sjAzdH3F1jpwtsAzdH3F9nc08%3F9nc08_ip4s%3D%267v%3D8cab8cma09&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
# url="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9C%A3%E5%BD%BC%E5%BE%97%E5%A4%A7%E6%95%99%E5%A0%82&step_word=&hs=2&pn=6&spn=0&di=200150222910&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=3041482675%2C4051962764&os=3787562976%2C844574949&simid=0%2C0&adpicid=0&lpn=0&ln=1998&fr=&fmq=1553568712019_R&fm=detail&ic=undefined&s=undefined&hd=&latest=&copyright=&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2Ftg%2F314%2F363%2F443%2Fe31656bb560849c195f7c912077f2cae_R_1024_10000_Q90.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fy57_z%26e3Bkt2c_z%26e3Bvp6tr_z%26e3Bv54AzdH3Fp6wejsfAzdH3Fewptvwg0b9AzdH3F8l8nacn_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
# print("11111")
#
# # 打开谷歌浏览器Chrome
# browser = webdriver.Chrome()
# browser.get(url)
# print("222")
#
# # 设置下载的图片数量及进行下载
# start = 1
# end = 800
# for i in range(start,end + 1):
# #     # 获取图片位置
#     img = browser.find_elements_by_xpath("//img[@class='currentImg']")
#     print("333")
#     for ele in img:
#         #   获取图片链接
#         target_url = ele.get_attribute("src")
#         print(target_url)
#         #   设置图片名称。以图片链接中的名字为基础选取最后25个字节为图片名称。
#         img_name = target_url.split('/')[-1]
#         filename = os.path.join(path, img_name[-25:])
#         if "jpg" in filename:
#             download(target_url, filename)
# #     # 下一页
#     next_page = browser.find_element_by_class_name("img-next").click()
#     time.sleep(3)
# #     # 显示进度
#     print('%d / %d' % (i, end))
#
# # 关闭浏览器
# browser.quit()


def auto_download(path_list,url_list):
    for i in range(len(path_list)):
        if os.path.exists(path_list[i]) is False:
            os.makedirs(path_list[i])
        browser = webdriver.Chrome()
        browser.get(url_list[i])

        start = 1
        end = 2
        for i in range(start, end + 1):
            #     # 获取图片位置
            img = browser.find_elements_by_xpath("//img[@class='currentImg']")
            print("333")
            for ele in img:
                #   获取图片链接
                target_url = ele.get_attribute("src")
                print(target_url)
                #   设置图片名称。以图片链接中的名字为基础选取最后25个字节为图片名称。
                img_name = target_url.split('/')[-1]
                filename = os.path.join(path_list[i], img_name[-25:])
                if "jpg" in filename:
                    download(target_url, filename)
                    #     # 下一页
            next_page = browser.find_element_by_class_name("img-next").click()
            time.sleep(3)
            #     # 显示进度
            print('%d / %d' % (i, end))

        # 关闭浏览器
        browser.quit()

auto_download(path_list,url_list)
