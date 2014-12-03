import os
import time
import json
from Constants import Parameters
from pymongo import MongoClient

from collections import Counter,defaultdict
reviews_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][
    Parameters.REVIEWS_COLLECTION]

business_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][
    Parameters.BUSINESS_INFO_COLLECTION]


topic_rating_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.TOPIC_RATING_COLLECTION]
def getBest(num):
    count =  Counter();
    ave = Counter();
    res = defaultdict()
    for topic_id in range(60):
        result = topic_rating_collection.find({'ratings.'+str(topic_id):{'$exists':True}})
        temp =0
        for a in result:
             temp =temp+int(a['ratings'][str(topic_id)])
       # print temp
        ave[topic_id] =temp /result.count()
        count[topic_id] = result.count()
    #returns valid collection
    #print count.most_common(5)
    for id in count.most_common(num):
        res[id[0]] = (id[1],ave[id[0]])
    print res

getBest(10)
