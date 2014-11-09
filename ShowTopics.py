__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora


from Constants import Parameters


dictionary = corpora.Dictionary.load(Parameters.Dictionary_path)
corpus = corpora.MmCorpus(Parameters.Corpus_path)
lda = LdaModel.load(Parameters.Lda_model_path)

i = 0
for topic in lda.show_topics(num_topics=Parameters.Lda_num_topics):
    print '#' + str(i) + ': ' + topic
    i += 1