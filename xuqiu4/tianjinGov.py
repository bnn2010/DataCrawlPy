#北京市环保局数据，关键词： 京津冀 大气污染
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import requests
from bs4 import BeautifulSoup
from util import mongoUtil, htmlArticleUtil
#数据表：
coll = mongoUtil.getCollection('tianjinGov')
def tianjinGovData():
    headers = {'content-type': 'application/xhtml+xml',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    count=0
    #注意：实际上显示的结果有20多页，但是“京津冀”和“大气污染”都有的只有前11页。
    for i in range(1,22):

        # url = 'http://so.beijing.gov.cn/s?q=1&qt=%E4%BA%AC%E6%B4%A5%E5%86%80and%E5%A4%A7%E6%B0%94%E6%B1%A1%E6%9F%93&pageSize=10&database=all&page='+str(i)+'#gettop'
        url = 'http://search.tj.gov.cn/s?q=1&qt=%E4%BA%AC%E6%B4%A5%E5%86%80+%E5%A4%A7%E6%B0%94%E6%B1%A1%E6%9F%93&pageSize=10&database=all&page='+str(i)+'#gettop'
        htmlMeta=requests.get(url,headers=headers)
        soup = BeautifulSoup(htmlMeta.text, "lxml")
        # print(soup)
        # break
        page_content = soup.find("div","center_side")
        # print(page_content)
        # break
        itemList = page_content.find_all("div","list")
        for item in itemList:
            count += 1
            print("count:", count)
            # print(item)
            title=item.find('a').text
            showhref='http://so.beijing.gov.cn/'+item.find('a')['href']
            href=processJiaMiUrl(showhref)
            abstract=item.p.text
            publishTime=item.find_all('span')[-1].text
            # publishTime=publishTime.strip()
            cleanContent=htmlArticleUtil.getArticleFromHtml(href)
            # print("title:",title)
            # print("href:",href)
            # print("abstract:",abstract)
            # print("publishTime:",publishTime)
            # print("cleanContent:",cleanContent)
            doc = {'title': title, 'publish_time': publishTime,'url':href,'abstract':abstract,'cleanContent':cleanContent}
            coll.insert(doc)
            # break

        # title=page_content.
        # print(page_content)



def processJiaMiUrl(url):
    # url='http://so.beijing.gov.cn/view?qt=%E4%BA%AC%E6%B4%A5%E5%86%80and%E5%A4%A7%E6%B0%94%E6%B1%A1%E6%9F%93&location=81&reference=6d5f596bbf3c09e84efa9a31deb5fc66&url=1BF35E1A375D90B987109D42A14412DF8113A739F20381FA76F56901BC230579FE754BA6F593E514ED2F949A43B43F39D07083531B33DB21&title=%E4%BA%AC%E6%B4%A5%E5%86%80%E6%9C%80%E5%A4%A7%E8%BF%9B%E5%8F%A3%E5%95%86%E5%93%81%E7%9B%B4%E8%90%A5%E4%B8%AD%E5%BF%83%E6%8C%82%E7%89%8C&database=all'
    # url='http://so.beijing.gov.cn/view?qt=%E4%BA%AC%E6%B4%A5%E5%86%80and%E5%A4%A7%E6%B0%94%E6%B1%A1%E6%9F%93&location=82&reference=272cb103c9e5fc7af63253cc36316e15&url=1BF35E1A375D90B9BD2C8B2D41B3F945AB7776326E07326EEC47D29FFB0EE58FCA04FC2E243AC3C3BA2D6B6EE359F00FCA9AEEA320C5BBFF&title=%E5%85%B3%E4%BA%8E%E8%BD%AC%E5%8F%91%E5%9B%BD%E5%AE%B6%E9%87%8D%E7%82%B9%E7%A0%94%E5%8F%91%E8%AE%A1%E5%88%92%E2%80%9C%E5%A4%A7%E6%B0%94%E6%B1%A1%E6%9F%93%E6%88%90%E5%9B%A0%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%8A%80%E6%9C%AF%E7%A0%94%E7%A9%B6%E2%80%9D%E7%AD%894%E4%B8%AA%E9%87%8D%E7%82%B9%E4%B8%93%E9%A1%B92017%E5%B9%B4%E5%BA%A6%E5%AE%9A%E5%90%91%E9%A1%B9%E7%9B%AE%E7%94%B3%E6%8A%A5%E8%A6%81%E6%B1%82%E7%9A%84%E9%80%9A&database=all'
    headers = {'content-type': 'application/xhtml+xml',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, "lxml")
    strData=str(soup.body)
    href,_=strData[36:].split('\');\">')
    return href

    # print(href)
    # print(soup.children.text)
    # href=soup.find('a')
    #
    # print(href)


tianjinGovData()
# processJiaMiUrl()