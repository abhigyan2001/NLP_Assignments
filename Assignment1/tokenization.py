from util import *

# Add your import statements here
import re



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = [[] for i in range(len(text))]

		#Fill in code here
		for i,sentence in enumerate(text):
			sentence = re.sub('\'|\"|\(|\)|,|;|\[|\]|\{|\}|\.|\?|!', ' ', sentence).strip()
			tokenizedText[i] = sentence.split()
		return tokenizedText

	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		return tokenizedText

# txt = ["nlp,(txt) 'lol' \"lmao\" [asdasd]{asda}]} "]
# print(Tokenization().naive(txt))