__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora


import Constants


dictionary = corpora.Dictionary.load(Constants.Dictionary_path)
corpus = corpora.MmCorpus(Constants.Corpus_path)
lda = LdaModel.load(Constants.Lda_model_path)

i = 0
for topic in lda.show_topics(num_topics=Constants.Lda_num_topics):
    print '#' + str(i) + ': ' + topic
    i += 1