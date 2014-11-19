from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk
from Constants import Parameters
__author__ = 'Parry'
import os
import time
import json



corpus_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.CORPUS_COLLECTION]
reviews_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.REVIEWS_COLLECTION]


stopset = set(stopwords.words('english'))

lmtzr = WordNetLemmatizer()
review_cursor = reviews_collection.find()
print review_cursor.count()
stopwords = {}
with open('stopwords.txt', 'rU') as f:
    for line in f:
        stopwords[line.strip()] = 1
print stopwords
for i in range(review_cursor.count()):
        try :
             review =review_cursor.__getitem__(i)
        except Exception:
             print 'Exceptions..!!!!!!'
             continue

        words = []

        sentences = nltk.sent_tokenize(review['text'].lower())
        for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                filteredWords = [word for word in tokens if word not in stopwords]
                tagged_text = nltk.pos_tag(filteredWords)

                for word, tag in tagged_text:
                    if tag in ['NN','NNS'] :
                        words.append(lmtzr.lemmatize(word))

        corpus_collection.insert({
              "reviewId": review["reviewId"],
              "business": review["business"],
              "stars": review['stars'],
              "votes":review["votes"],
              "text": review["text"],
              "words": words
        })

