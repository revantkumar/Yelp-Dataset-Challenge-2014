from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk

__author__ = 'Parry'
import os
import time
import json

DATASET_FILE = '../yelp_dataset_challenge_academic_dataset-1/'
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
REVIEWS_DATABASE = "Dataset_Challenge_Reviews"
CORPUS_COLLECTION = "Corpus"
REVIEWS_COLLECTION = "Reviews"

corpus_collection = MongoClient(MONGO_CONNECTION_STRING)[REVIEWS_DATABASE][CORPUS_COLLECTION]
reviews_collection = MongoClient(MONGO_CONNECTION_STRING)[REVIEWS_DATABASE][REVIEWS_COLLECTION]

stopset = set(stopwords.words('english'))

lmtzr = WordNetLemmatizer()
review_cursor = reviews_collection.find()
print review_cursor.count()
for review in review_cursor:
    words = []
    try :
        sentences = nltk.sent_tokenize(review['text'].lower())
        for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                filteredWords = [word for word in tokens if word not in stopset]
                tagged_text = nltk.pos_tag(filteredWords)

                for word, tag in tagged_text:
                    if tag in ['NN','NNS']:
                        words.append(lmtzr.lemmatize(word))

        corpus_collection.insert({
              "reviewId": review["reviewId"],
              "business": review["business"],
              "stars": review['stars'],
              "votes":review["votes"],
              "text": review["text"],
              "words": words
        })

    except Exception:
            print 'Exceptions..!!!!!!'