import sklearn.metrics as met
import pandas as pd
from nltk.tokenize import word_tokenize
import func_similarityfunc as sim
import func_tfidf as tfidf
import func_datapreprocessing as pp
import func_predict as pred 
import numpy as np

def print_recipe(row,df_recip):
    rd_recipe = df_recip 
    print("Recipe name")
    print(pp.preprocess(rd_recipe['recipe_name'][row]))
    print(" ")
    print("Cooking directions")
    print(pp.preprocess(rd_recipe['cooking_directions'][row]))
    print(" ")
    print("Ingredients")
    print(pp.preprocess(rd_recipe['ingredients'][row]))
    print(" ")

def user_rate(user_id,df_inter, df_recip):
    rd_interaction = df_inter
    rd_recipe = df_recip

    join_header = ['recipe_id', 'recipe_name']
    rd_name = rd_recipe[join_header]
    merged_inner = pd.merge(left=rd_name, right=rd_interaction)
    filter = rd_interaction['user_id'] == user_id
    user_int = merged_inner.loc[filter, :]
    return user_int

def print_PrecRec_eval(user_query, model_df):   
    eval_df = model_df

    evalmodel_text = []    #processed text of the model dataset
    for text in eval_df['cooking_directions']:
        evalmodel_text.append(word_tokenize(pp.preprocess(text)))

    print("query is: " + user_query)
    [dataset, dict_vocab, N] = tfidf.vectorize_corpus(evalmodel_text)
    
    [Q,score] = pred.cosine_similarity(7, user_query, dataset, dict_vocab, N)
    print("index,   recipe_id,    recipe name,   user rating,   similarity score")
    n = 0 
    for i in Q:
        recipname = pp.preprocess(eval_df['recipe_name'][i])
        averate = np.around(eval_df['rating'][i],2)
        simscore = np.around(score[n]*100,2)
        recipid = eval_df['recipe_id'][i]
        print( str(i) + "   " + str(recipid) + "   " + str(recipname)  +  "   " +  str(averate) + "   " + str(simscore))
        n += 1

