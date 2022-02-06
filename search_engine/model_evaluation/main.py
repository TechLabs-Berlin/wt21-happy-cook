import sys
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from collections import Counter
import advertools as adv
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words
import os
import numpy as np
import pandas as pd



import func_similarityfunc as sim
import func_tfidf as tfidf
import func_datapreprocessing as pp
import func_predict as pred 


rd_recipe = pd.read_csv('ds_dataset/raw-data_recipe.csv')

#use Ganyi's function here to clean data

processed_text = []
for text in rd_recipe['cooking_directions']:
    processed_text.append(word_tokenize(pp.preprocess(text)))

user_query = str(input("Write a query:"))

[D, DF, N] = tfidf.vectorize_corpus(processed_text)
[ model , model_score] = pred.cosine_similarity(10, user_query, D , DF, N)
