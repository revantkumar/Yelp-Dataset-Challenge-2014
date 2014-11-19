
from pymongo import MongoClient

__author__ = 'Parry'
from gensim.models import LdaModel
from gensim import corpora
from Constants import Parameters
from nltk import WordNetLemmatizer
from pymongo import MongoClient
from nltk.corpus import stopwords
import nltk

dictionary = corpora.Dictionary.load(Parameters.Dictionary_path)
corpus = corpora.BleiCorpus(Parameters.Corpus_path)
lda = LdaModel.load(Parameters.Lda_model_path)




Review ="It's like eating with a big Italian family. " \
                 "Great, authentic Italian food, good advice when asked, and terrific service. " \
                 "With a party of 9, last minute on a Saturday night, we were sat within 15 minutes. " \
                 "The owner chatted with our kids, and made us feel at home. " \
                 "It was an overall great experience!"
stopset = set(stopwords.words('english'))
words = []
lmtzr = WordNetLemmatizer()
sentences = nltk.sent_tokenize(Review.lower())
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    filteredWords = [word for word in tokens if word not in stopset]
    tagged_text = nltk.pos_tag(filteredWords)
    for word, tag in tagged_text:
          if tag in ['NN','NNS']:
              words.append(lmtzr.lemmatize(word))

print lda[dictionary.doc2bow(words)]