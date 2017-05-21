#北京市环保局数据，关键词： 京津冀 大气污染
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import requests
from bs4 import BeautifulSoup
from util import mongoUtil, htmlArticleUtil
#数据表：
coll = mongoUtil.getCollection('bjepb')
def bjepbData():
    headers = {'content-type': 'application/xhtml+xml',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    count=0
    #注意：实际上显示的结果有20多页，但是“京津冀”和“大气污染”都有的只有前11页。
    for i in range(1,12):

        url = 'http://www.bjepb.gov.cn/dig/search.action?ty=&w=false&f=&dr=true&p='+str(i)+'&sr=score+desc&rp=szns&advtime=&advrange=&fq=&q=%E4%BA%AC%E6%B4%A5%E5%86%80+%E5%A4%A7%E6%B0%94%E6%B1%A1%E6%9F%93'
        htmlMeta=requests.get(url,headers=headers)
        soup = BeautifulSoup(htmlMeta.text, "lxml")
        # print(soup)
        page_content = soup.find("div","cen_list")
        itemList = page_content.find_all("ul")
        for item in itemList:
            count += 1
            print("count:", count)
            # print(item)
            title=item.h3.text
            href=item.h3.a['href']
            abstract=item.p.text
            _,publishTime=item.li.text.split('..')
            publishTime=publishTime.strip()
            cleanContent=htmlArticleUtil.getArticleFromHtml(href)
            # print("title:",title)
            # print("href:",href)
            # print("abstract:",abstract)
            # print("publishTime:",publishTime)
            # print("cleanContent:",cleanContent)
            doc = {'title': title, 'publish_time': publishTime,'url':href,'abstract':abstract,'cleanContent':cleanContent}
            coll.insert(doc)

        # title=page_content.
        # print(page_content)




bjepbData()