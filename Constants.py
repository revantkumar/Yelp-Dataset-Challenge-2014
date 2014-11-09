__author__ = 'Parry'
class Parameters:
    def __init__(self):
        pass


    DATASET_FILE = '../yelp_dataset_challenge_academic_dataset/'
    MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
    REVIEWS_DATABASE = "Dataset_Challenge_Reviews"
    REVIEWS_COLLECTION = "Reviews"
    BUSINESS_COLLECTION = 'Business'

    CORPUS_COLLECTION = "Corpus"

    Dictionary_path = "DataModels/dictionary.dict"
    Corpus_path = "DataModels/corpus.mm"
    Lda_num_topics = 20
    Lda_model_path = "DataModels/lda_model_topics.lda"