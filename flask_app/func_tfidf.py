from tracemalloc import DomainFilter
import numpy as np
from collections import Counter
import math


def doc_freq(word, DF):  # counts how in how many documents does each word come up
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c

def gen_vector(tokens, DF ,N):  #this is the generate vector of the query
    total_vocab = [x for x in DF]
    
    
    Q = np.zeros((len(total_vocab)))
    
    counter = Counter(tokens)
    words_count = len(tokens)

    query_weights = {}
    
    for token in np.unique(tokens):
        
        tf = counter[token]/words_count
        df = doc_freq(token, DF)
        idf = math.log((N+1)/(df+1))

        try:
            ind = total_vocab.index(token)
            Q[ind] = tf*idf
        except:
            pass
        
    return Q



def vectorize_corpus(processed_text): #vectorizes the whole recipe collection in dataset
	
	DF = {}
	N = len(processed_text)
	for i in range(N):
		tokens = processed_text[i]
    
		for w in tokens:
			#print(w)
			try:
				DF[w].add(i)
			except:
				DF[w] = {i}

	for i in DF:
		DF[i] = len(DF[i])
	
	total_vocab_size = len(DF)
	total_vocab = [x for x in DF]
	

	doc = 0

	tf_idf = {}

	for i in range(N):
		tokens = processed_text[i]
    
		counter = Counter(tokens)
		words_count = len(tokens)
    
		for token in np.unique(tokens):

			tf = counter[token]/words_count
			df = doc_freq(token, DF)


			idf = np.log((N+1)/(df+1))
        
			tf_idf[doc, token] = tf*idf
		doc += 1
	
	D = np.zeros((N, total_vocab_size))
	for i in tf_idf:
		try:
			ind = total_vocab.index(i[1])
			D[i[0]][ind] = tf_idf[i]
		except:
			pass

	return D, DF , N   #D is the collection of recipe vectors , DF is the document frequency for each word, N is the length of the collection of recipes
