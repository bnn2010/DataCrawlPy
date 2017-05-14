import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import requests
from bs4 import BeautifulSoup

import urllib

from util import mongoUtil

coll = mongoUtil.getCollection('lawxy')

#借助site:gov.cn  来寻找政府网址。
def getLawxpData(RegionId,keyword,page):
    param = {'RegionId':RegionId,'q':keyword,'pg':page}
    query='http://www.lawxp.com/statute/?'+urllib.parse.urlencode(param)
    print(query)
    page = requests.get(query)
    soup = BeautifulSoup(page.text,"lxml")
    page_content=soup.find("div","xfg-news1")
    # print(page_content)
    liList = page_content.find_all('li')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    for li in liList:
        #文件标题
        title= li.find('div','zyin-ll-bt1').a.text
        #发布字号
        publishId = li.find('span','zyin-ll-bt2').text.replace('发布字号：','')
        #发布机构
        publishOffice = li.find('div','fleft zyin-fbjg').text.replace('发布机构：','')
        publishTime = li.find('div','zyin-ll-rq fright').text[5:15]
        print('Id:',publishId)
        print('-----------------------------------------')
        print('time:',publishTime)
        print('----------------------------------------')
        print('title:',title)
        print('-----------------------------------------')
        # print(li)
        print('office:',publishOffice)
        print('----------------------------------------------------------')
        doc={'文件标题':title,'发布字号':publishId,'发布机构':publishOffice,'发布时间':publishTime}
        coll.insert(doc)


if __name__=='__main__':
    #2:北京，
    #100000:中央
    #3:天津
    #4:河北
    #6:内蒙古
    #5:山西
    #16:山东
    #
    RegionId='100000'
    keyword='大气'
    page=1
    size=6
    for i in range(1,size+1):
        getLawxpData(RegionId,keyword,i)
