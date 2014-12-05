User Manual
-----------

Configuration used for executing scripts and deploying the application:
Python Version - 2.7.6
MongoDB Version - 2.6.5

Installation
------------
- Download and extract the source files from http://a.ashwinikhare.in/yelpolo.tar.gz (Warning : consists of all yelp reviews, File Size > 350 MB)

- The following steps perform various computations to generate Topics & a link of database dump is provided in the end.

	- python Loader.py
		- Depency - pymongo. Run `pip install pymongo`
		- Populates the reviews for Phoenix from the dataset json where type of business equals to the restaurant

	- python Normalizer.py
		- Dependency - nltk. Run `pip install nltk`. Also nltk corpus data, So need to import nltk and run nltk.download() in a python shell
		- Makes Reviews more simplified for Online Analysis

	- python OnlineLDA.py
		- Dependency - gensim. Run `pip install gensim`
		- Gensim python library creates a LDA model for different reviews.

	- python ShowTopics.py
		- Displays the six major topics and the sub-topics with maximum weightages Respectively
		- All 60 topics were categorised so as to highlight the sub-topic they represent
		- The 60 subtopics highlighted in _topics.txt_

	The required data is now computed and a few auxiliary scripts are present in the .tar.gz which are used to generate other graphs like Business Frequency Topic was plotted by data generated using : `getFreqBusinessTopic.py`

	The database dump which was computed in our evaluation can be downloaded from http://a.ashwinikhare.in/archive.tar.gz and can be directly imported into the mongodb by adjusting suitable paramters in Constants.py

-Running the Graphical User Interface
	
	- python 'getBusinessTopic.py'
		- Dependency - bottle. Run `pip install bottle`
		- Creates a web server listening at 0.0.0.0:8030 which renders the application
	- A live deployed link is present on the server, accessible at http://a.ashwinikhare.in:8030/yelpolo
