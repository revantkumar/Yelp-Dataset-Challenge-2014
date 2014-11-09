__author__ = 'Parry'

from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk
import gensim
from gensim import corpora
from Constants import Parameters



corpus_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.CORPUS_COLLECTION]


corpus_cursor = corpus_collection.find()



class MyCorpus(object):
    def __iter__(self):
         for review in corpus_cursor:
             yield dictionary.doc2bow(review["words"])


dictionary = corpora.Dictionary(review['words'] for review in corpus_cursor)
dictionary.compactify()
corpora.Dictionary.save(dictionary,Parameters.Dictionary_path)
corpus = MyCorpus()
corpora.MmCorpus.serialize(Parameters.Corpus_path,corpus)

lda = gensim.models.LdaModel(corpus, num_topics=Parameters.Lda_num_topics, id2word=dictionary)
lda.save(Parameters.Lda_model_path)