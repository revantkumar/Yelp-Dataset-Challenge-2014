__author__ = 'Parry'

from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk
import gensim
from gensim import corpora
from Constants import Parameters

from gensim.corpora import BleiCorpus

corpus_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.CORPUS_COLLECTION]


corpus_cursor = corpus_collection.find()

mycorpus_cursor = corpus_collection.find()

class MyCorpus(object):
    def __iter__(self):
     #    print 'test'
         for review in mycorpus_cursor:
            # print 'here'
             yield dictionary.doc2bow(review["words"])

print corpus_cursor.count()

dictionary = corpora.Dictionary(review['words'] for review in corpus_cursor)
dictionary.filter_extremes(keep_n=10000)
dictionary.compactify()
corpora.Dictionary.save(dictionary,Parameters.Dictionary_path)
#corpus = MyCorpus()
ncorpus =[]
for review in mycorpus_cursor:
            # print 'here'
             ncorpus.append(dictionary.doc2bow(review["words"]))
corpora.BleiCorpus.serialize(Parameters.Corpus_path,ncorpus)
dcorpus = corpora.BleiCorpus(Parameters.Corpus_path)
lda = gensim.models.LdaModel(dcorpus, num_topics=Parameters.Lda_num_topics, id2word=dictionary)
lda.save(Parameters.Lda_model_path)
i=0
for topic in lda.show_topics(num_topics=Parameters.Lda_num_topics):
    print '#' + str(i) + ': ' + topic
    i += 1
