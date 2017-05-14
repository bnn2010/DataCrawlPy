from util import mongoUtil


#获取文件名
# import pymongo
def processPaperName():
    coll = mongoUtil.getCollection('CrawledData_3')
    paperTitleSet=set()
    for doc in coll.find():
        # print(doc)
        paperTitle = doc['paperTitle']
        paperTitle = paperTitle.replace('\n','')
        # print('before:',paperTitle)
        paperList = paperTitle.split('#')
        # print('after:',paperList)
        for item in paperList:
            if len(item)>=3:
                paperTitleSet.add(item)
    collInsert = mongoUtil.getCollection('CrawledData_4')
    for it in paperTitleSet:
        print(it)
        #降序pymongo.DESCENDING
        firstOne = coll.find({'paperTitle':{'$regex':it}}).sort('publish_time').limit(1)

        for one in firstOne:
            # insertOne={''}
            try:
                collInsert.insert(one)
            except Exception as e:
                continue
        print('-----------------------------------------------------------')



if __name__=='__main__':
    # s= '意见'
    # print(len(s))
    processPaperName()

