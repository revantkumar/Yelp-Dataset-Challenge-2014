__author__ = 'Parry'

from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk
import gensim
from gensim import corpora
import Constants



corpus_collection = MongoClient(Constants.MONGO_CONNECTION_STRING)[Constants.REVIEWS_DATABASE][Constants.CORPUS_COLLECTION]


corpus_cursor = corpus_collection.find()



class MyCorpus(object):
    def __iter__(self):
         for review in corpus_cursor:
             yield dictionary.doc2bow(review["words"])


dictionary = corpora.Dictionary(review['words'] for review in corpus_cursor)
dictionary.compactify()
corpora.Dictionary.save(dictionary,Constants.Dictionary_path)
corpus = MyCorpus()
corpora.MmCorpus.serialize(Constants.Corpus_path,corpus)

lda = gensim.models.LdaModel(corpus, num_topics=Constants.Lda_num_topics, id2word=dictionary)
lda.save(Constants.Lda_model_path)