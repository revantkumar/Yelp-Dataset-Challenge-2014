__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora


from Constants import Parameters


dictionary = corpora.Dictionary.load(Parameters.Dictionary_path)
corpus = corpora.BleiCorpus(Parameters.Corpus_path)
lda = LdaModel.load(Parameters.Lda_model_path)
print lda
i = 0


print lda.num_topics

print ''
print '$$$$$$$$$$$$$$$$$$'
for topic in lda.show_topics(num_topics=Parameters.Lda_num_topics):
    print '#' + str(i) + ': ' + topic
    i += 1