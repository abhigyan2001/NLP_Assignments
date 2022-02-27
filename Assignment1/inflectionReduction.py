from util import *

# Add your import statements here
from nltk.stem.snowball import SnowballStemmer
  
#the stemmer requires a language parameter
snow_stemmer = SnowballStemmer(language='english')

# from nltk.stem import PorterStemmer
  
# ps = PorterStemmer()

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = [[0 for j in range(len(text[i]))] for i in range(len(text))]
		
		reducedText2 = [[0 for j in range(len(text[i]))] for i in range(len(text))]
		#Fill in code here
		for i,sentence in enumerate(text):
			for j,word in enumerate(sentence):
				#reducedText[i][j] = ps.stem(word)
				reducedText2[i][j] = snow_stemmer.stem(word)

		return reducedText,reducedText2

# choose some words to be stemmed
# words = [["program", "programs"],["programmer","teeth"], ["leaves","fairly","frankly","children","programming", "programmers"]]

# print(InflectionReduction().reduce(words))