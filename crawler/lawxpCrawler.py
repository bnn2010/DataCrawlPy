import requests
from bs4 import BeautifulSoup

import urllib
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
        publishTime = li.find('div','zyin-ll-rq fright').text[5:16]
        print('Id:',publishId)
        print('-----------------------------------------')
        print('time:',publishTime)
        print('----------------------------------------')
        print('title:',title)
        print('-----------------------------------------')
        # print(li)
        print('office:',publishOffice)
        print('----------------------------------------------------------')


# import urllib2
# import urllib
# def baidu_search(keyword,pn):
#     p= {'wd': keyword}
#     res=urllib2.urlopen(("http://www.baidu.com/s?"+urllib.urlencode(p)+"&pn={0}&cl=3&rn=100").format(pn))
#     html=res.read()
#     return html


if __name__=='__main__':
    RegionId='2'
    keyword='大气'
    page=1
    getLawxpData(RegionId,keyword,page)
