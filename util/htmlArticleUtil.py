#coding:utf-8
import newspaper
from newspaper import Article
# print(newspaper.languages())
# print(newspaper.popular_urls())
# Article.build(self)
from DataProcess import processData
from util import mongoUtil

#核心工具
def getArticleFromHtml(html):
    try:
        content = Article(html,language='zh')
        content.download()
        content.parse()
        return content.text
    except Exception as e:
        pass
    # print(content.meta_keywords)



def getCleanContent2Mongo():
    coll = mongoUtil.getCollection('lp')
    results = coll.find()
    count = 0
    for result in results:
        count+=1
        print(count)
        html = result['URL']
        cleanContent=getArticleFromHtml(html)
        coll.update_one({'URL':html},{"$set":{'cleanContent':cleanContent}})



def getKeyWords2Mongo():
    coll = mongoUtil.getCollection('CrawledData_4')
    results = coll.find()
    count = 0
    keyWordsList = ['京津冀','大气污染','雾霾','区域协作','统筹','会商','协调','联动','助力']
    # with open('D:\PycharmProjects\DataCrawl\data\keywords.txt','rb') as f:
    #     for line in f.readlines():
    #         word = line.strip()
    #         word = word.encode('utf-8')
    #         keyWordsList.append(word)
    for result in results:
        # print(result['title'])
        print(result)
        # break
        count+=1
        print(count)
        try:
            if result['cleanContent']:

                cleanContent = result['cleanContent']
                print(cleanContent)

                keyWords=processData.getKeywords(cleanContent, keyWordsList)
                print('------------------------------')

                keyword =','.join(keyWords)
                print(keyword)
                coll.update_one({'_id':result['_id']},{"$set":{'keyword':keyword}})
        except Exception as e:
            continue



def updateOne(html):
    coll = mongoUtil.getCollection('CrawledData_3')

    cleanContent = getArticleFromHtml(html)
    coll.update_one({'source_url': html}, {"$set": {'cleanContent': cleanContent}})

def updateAll():
    coll = mongoUtil.getCollection('CrawledData_3')
    results = coll.find()
    for result in results:
        url = result['url']



def delete_one():
    coll = mongoUtil.getCollection('CrawledData_3')
    results = coll.find()
    for result in results:
        print(len(result))
        try:
            cleanContent=result['cleanContent']
        except Exception as e:
            coll.delete_one({"id":result['id']})
    # coll.find_one_and_delete({'cleanContent':None})



if __name__=='__main__':

    # getArticleFromHtml(html)
    # getCleanContent2Mongo()
    getKeyWords2Mongo()
    # updateOne(html)
    # delete_one()

