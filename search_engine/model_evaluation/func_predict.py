import numpy as np
from collections import Counter
from nltk.tokenize import word_tokenize
from collections import Counter
import os
import numpy as np

import func_similarityfunc as sim
import func_tfidf as tfidf
import func_datapreprocessing as pp

def cosine_similarity(k, query, dataset, dict_vocab, N):
    preprocessed_query = pp.preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))
    
    
    d_cosines = []
    
    query_vector = tfidf.gen_vector(tokens, dict_vocab, N)
    
    for d in dataset:
        d_cosines.append(sim.cosine_sim(query_vector, d))
        
    score = np.sort(np.array(d_cosines))[-k:][::-1]
    out = np.array(d_cosines).argsort()[-k:][::-1]
    
    return out,score 

def euclidean_similarity(k, query, dataset, dict_vocab, N):
    preprocessed_query = pp.preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))
    
    
    d_cosines = []
    
    query_vector = tfidf.gen_vector(tokens, dict_vocab, N)
    
    for d in dataset:
        d_cosines.append(sim.euclidean_sim(query_vector, d))
        
    score = np.sort(np.array(d_cosines))[-k:][::-1]
    out = np.array(d_cosines).argsort()[-k:][::-1]
    
    return out,score 