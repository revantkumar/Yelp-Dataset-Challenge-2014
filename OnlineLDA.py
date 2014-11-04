__author__ = 'Parry'

from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk
import gensim
from gensim import corpora

dictionary_path = "DataModels/dictionary.dict"
corpus_path = "DataModels/corpus.mm"
lda_num_topics = 20
lda_model_path = "DataModels/lda_model_topics.lda"

DATASET_FILE = '../yelp_dataset_challenge_academic_dataset-1/'
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
REVIEWS_DATABASE = "Dataset_Challenge_Reviews"
CORPUS_COLLECTION = "Corpus"

corpus_collection = MongoClient(MONGO_CONNECTION_STRING)[REVIEWS_DATABASE][CORPUS_COLLECTION]


corpus_cursor = corpus_collection.find()



class MyCorpus(object):
    def __iter__(self):
         for review in corpus_cursor:
             yield dictionary.doc2bow(review["words"])


dictionary = corpora.Dictionary(review['words'] for review in corpus_cursor)
dictionary.compactify()
corpora.Dictionary.save(dictionary,dictionary_path)
corpus = MyCorpus()
corpora.MmCorpus.serialize(corpus_path,corpus)

lda = gensim.models.LdaModel(corpus, num_topics=lda_num_topics, id2word=dictionary)
lda.save(lda_model_path)