

#添加关键词字段
#获取关键词。
def getKeywords(content,wordList):
    resultList = []
    for item in wordList:
        if item in content:
            resultList.append(item)
    return resultList





