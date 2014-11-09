from pymongo import MongoClient

__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora
import Constants



dictionary = corpora.Dictionary.load(Constants.Dictionary_path)
corpus = corpora.MmCorpus(Constants.Corpus_path)
lda = LdaModel.load(Constants.Lda_model_path)



corpus_collection = MongoClient(Constants.MONGO_CONNECTION_STRING)[Constants.REVIEWS_DATABASE][Constants.CORPUS_COLLECTION]

i=0
corpus_cursor = corpus_collection.find()
for review in corpus_cursor:
             # assume there's one document per line, tokens separated by whitespace
             i=i+1
             print lda[dictionary.doc2bow(review["words"])]
             if i ==20:
                 break;


