import os
import time
import json
from Constants import Parameters
from pymongo import MongoClient


reviews_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][
    Parameters.REVIEWS_COLLECTION]

business_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][
    Parameters.BUSINESS_COLLECTION]


with open(Parameters.DATASET_FILE +'yelp_academic_dataset_business.json') as dataset:
    for line in dataset:

            data = json.loads(line)

            if 'Restaurants' in data["categories"] and data['city'] == 'Phoenix':
               business_collection.insert({
                 "_id": data["business_id"]
               })


with open(Parameters.DATASET_FILE +'yelp_academic_dataset_review.json') as dataset:
    for line in dataset:

            data = json.loads(line)
            isRestaurant = business_collection.find({"_id": data["business_id"]}).count();

            if data["type"] == "review"   and isRestaurant !=0:
                 reviews_collection.insert({
                "reviewId": data["review_id"],
                "business": data["business_id"],
                "text": data["text"],
                "stars": data['stars'],
                "votes":data["votes"]
                })