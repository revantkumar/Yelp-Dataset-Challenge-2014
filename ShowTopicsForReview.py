from pymongo import MongoClient

__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora
from Constants import Parameters



dictionary = corpora.Dictionary.load(Parameters.Dictionary_path)
corpus = corpora.BleiCorpus(Parameters.Corpus_path)
lda = LdaModel.load(Parameters.Lda_model_path)



corpus_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.CORPUS_COLLECTION]

i=0
corpus_cursor = corpus_collection.find()
for review in corpus_cursor:
             # assume there's one document per line, tokens separated by whitespace
             i=i+1
             print lda[dictionary.doc2bow(review["words"])]
             if i ==20:
                 break;


