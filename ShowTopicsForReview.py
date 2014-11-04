from pymongo import MongoClient

__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora



dictionary_path = "DataModels/dictionary.dict"
corpus_path = "DataModels/corpus.mm"
lda_num_topics = 20
lda_model_path = "DataModels/lda_model_topics.lda"

DATASET_FILE = '../yelp_dataset_challenge_academic_dataset-1/'
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
REVIEWS_DATABASE = "Dataset_Challenge_Reviews"
CORPUS_COLLECTION = "Corpus"

dictionary = corpora.Dictionary.load(dictionary_path)
corpus = corpora.MmCorpus(corpus_path)
lda = LdaModel.load(lda_model_path)



corpus_collection = MongoClient(MONGO_CONNECTION_STRING)[REVIEWS_DATABASE][CORPUS_COLLECTION]

i=0
corpus_cursor = corpus_collection.find()
for review in corpus_cursor:
             # assume there's one document per line, tokens separated by whitespace
             i=i+1
             print lda[dictionary.doc2bow(review["words"])]
             if i ==20:
                 break;


