__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora



dictionary_path = "DataModels/dictionary.dict"
corpus_path = "DataModels/corpus.mm"
lda_num_topics = 20
lda_model_path = "DataModels/lda_model_topics.lda"

dictionary = corpora.Dictionary.load(dictionary_path)
corpus = corpora.MmCorpus(corpus_path)
lda = LdaModel.load(lda_model_path)

i = 0
for topic in lda.show_topics(num_topics=lda_num_topics):
    print '#' + str(i) + ': ' + topic
    i += 1