import newspaper
from newspaper import Article
# print(newspaper.languages())
# print(newspaper.popular_urls())
# Article.build(self)
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
    coll = mongoUtil.getCollection('CrawledData_3')
    results = coll.find()
    count = 0
    for result in results:
        count+=1
        print(count)
        html = result['url']
        cleanContent=getArticleFromHtml(html)
        coll.update_one({'url':html},{"$set":{'cleanContent':cleanContent}})



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
    getCleanContent2Mongo()
    # updateOne(html)
    # delete_one()

