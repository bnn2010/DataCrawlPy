from pymongo import MongoClient
import datetime




client = MongoClient('mongodb://localhost:27017/tsinghua')
db = client['tsinghua']

def insert(collName,doc):
    coll = db[collName]
    # doc = {"author":"ning"}
    coll.insert(doc)

# 'CrawledData_3'
def update(collName,filter, update):
    coll = db[collName]
    coll.update_one(filter, update)
    
    
def getCollection(collName):
    coll = db[collName]
    return coll



if __name__=='__main__':
    insert()


