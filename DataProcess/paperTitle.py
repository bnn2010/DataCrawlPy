from util import mongoUtil


#获取文件名
# import pymongo
def processPaperName():
    coll = mongoUtil.getCollection('showData_second')
    paperTitleSet=set()
    for doc in coll.find():
        # print(doc)
        paperTitle = doc['paperTitle']
        paperList = paperTitle.split('#')
        for item in paperList:
            paperTitleSet.add(item)
