import numpy as np
import math

def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.

	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	N = len(corpus)
	df = [0] * len(query)

	for document in corpus:
		for q in enumerate(query):
			for word in document:
				if word == q[1]:
					df[q[0]] += 1
					break

	# print(df)
	tf_idf = []

	for document in corpus:
		tf_idf_i = []
		for q in enumerate(query):
			tf = 0
			for word in document:
				if word == q[1]:
					tf += 1

			tf /= len(document)
			idf = math.log((N + 1) / (df[q[0]] + 1)) + 1
			# print(idf)
			tf_idf_i.append(tf * idf)

		tf_idf.append(tf_idf_i)
	
	return tf_idf