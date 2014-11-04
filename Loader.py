import os
import time
import json

from pymongo import MongoClient

DATASET_FILE = '../yelp_dataset_challenge_academic_dataset-1/'
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
REVIEWS_DATABASE = "Dataset_Challenge_Reviews"
REVIEWS_COLLECTION = "Reviews"

reviews_collection = MongoClient(MONGO_CONNECTION_STRING)[REVIEWS_DATABASE][
    REVIEWS_COLLECTION]

with open(DATASET_FILE +'review.json') as dataset:
    for line in dataset:

            data = json.loads(line)

            if data["type"] == "review":
                 reviews_collection.insert({
                "reviewId": data["review_id"],
                "business": data["business_id"],
                "text": data["text"],
                "stars": data['stars'],
                "votes":data["votes"]
                })