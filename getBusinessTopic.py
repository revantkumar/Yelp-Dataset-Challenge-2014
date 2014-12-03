import os
import time
import json
from Constants import Parameters
from pymongo import MongoClient


reviews_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][
    Parameters.REVIEWS_COLLECTION]

business_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][
    Parameters.BUSINESS_INFO_COLLECTION]


topic_rating_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.TOPIC_RATING_COLLECTION]

topic_id = 50
def find_by_topic_id(topic_id, rating):
    
#result = topic_rating_collection.find_one()
    result = topic_rating_collection.find({'ratings.'+str(topic_id):{'$gt': int(rating) }})
#returns valid collection
    businesses = []
    for a in result:
        fetched_business = {}
        fetched_business['rating'] =  int(a['ratings'][str(topic_id)])
        b = business_collection.find_one({ '_id' : a['business'] })
        fetched_business['lat'] = b['lat']
        fetched_business['lon'] = b['lon']
        fetched_business['name'] = b['name']
        if fetched_business['rating'] > rating:
            businesses.append(fetched_business)
    return businesses
#print find_by_topic_id(50, 4)
#print businesses
#db.TopicRating.findOne({ "ratings.10" : { $exists: true }  })
#db.BusinessInfo.findOne({ '_id' : 'EmzaQR5hQlF0WIl24NxAZA'})
from bottle import route, run, template, static_file, response, request

@route('/')
def index():
    return 'Hello World'

@route('/getBusiness')
def getInfo():
    from bottle import response
    topic_id = request.query.topic_id
    rating = request.query.rating
    businesses = find_by_topic_id(topic_id, int(rating)-1)
    json_businesses = json.dumps(businesses)
    #response.content_type = 'application/json'
    return json_businesses

@route('/yelpolo')
def map():
    return static_file('visualization.html',root = './')
run(host='0.0.0.0', port='8030')
'''
{u'lat': 33.4795416, u'_id': u'x5Mv61CnZLohZWxfCVCPTQ', u'lon': -112.0734183, u'name': u"Domino's Pizza"}
'''
'''

with open(Parameters.DATASET_FILE +'yelp_academic_dataset_business.json') as dataset:
    for line in dataset:

            data = json.loads(line)

          
            if 'Restaurants' in data["categories"] and data['city'] == 'Phoenix':
               business_collection.insert({
                 "_id": data["business_id"],
                 "lat": data['latitude'],
                 "lon":data['longitude'],
                 "name":data['name']
               })o
'''
