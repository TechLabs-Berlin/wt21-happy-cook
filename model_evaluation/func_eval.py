
import sklearn.metrics as met
import pandas as pd
from nltk.tokenize import word_tokenize
import func_similarityfunc as sim
import func_tfidf as tfidf
import func_datapreprocessing as pp
import func_predict as pred 
import numpy as np

def query_class(num):
    if num == 1:
        user_query = "beef, salt, pepper"
    elif num == 2: 
        user_query = "chicken, cream"
    elif num == 3:
        user_query = "noodles, chicken"
    elif num == 4:
        user_query = "beef, potatoes"
    return user_query

def PrecRec_eval(model_df,threshold, prediction_model):  #written by Nisa Ulumuddin
    eval_df = model_df

    processed_text = []    #processed text of the model dataset
    for text in eval_df['cooking_directions']:
        processed_text.append(word_tokenize(pp.preprocess(text)))
    [dataset, dict_vocab, N] = tfidf.vectorize_corpus(processed_text)

    compiled_relevancy_score = []
    recipe_list = []
    rec_df = pd.DataFrame(columns=['Query1','sim_score_1','Query2','sim_score_2','Query3','sim_score_3','Query4','sim_score_4'])
    print("Performing 4 queries on the model dataset...")
    print("Query 1 : beef, salt, pepper ")
    print("Query 2 : chicken, cream ")
    print("Query 3 : noodles, chicken ")
    print("Query 4 : beef, potatoes ")
    num = 0 
    for query_num in range(1,5): #range(1,5)
        user_query = query_class(int(query_num))
        if prediction_model == "cosine_similarity":        
            [Q,score] = pred.cosine_similarity(threshold, user_query, dataset, dict_vocab, N)
        elif prediction_model == "euclidean_similarity":
            [Q,score] = pred.euclidean_sim(threshold, user_query, dataset, dict_vocab, N)
        else:
            print("did not submit a prediction model")
            exit()
        
        eval_reindex_df = eval_df.reindex(Q)
        header_name = str("Query ") + str(query_num)
        y_pred = [1,1,1,1,1,1,1]
        y_true = np.array(eval_reindex_df[header_name][0:threshold]) 
        compiled_relevancy_score.append(y_true)
        recipe_list.append(eval_reindex_df['recipe_name'][0:threshold].values.tolist())
        rec_df.iloc[:, num] = eval_reindex_df['recipe_name'][0:threshold].values.tolist()
        rec_df.iloc[:,num+1] = score
        num +=2 
        #print(eval_reindex_df['recipe_name'][0:threshold])
        #precision.append(met.precision_score(y_true, y_pred, average='weighted', zero_division = 0))
        #recall.append(met.recall_score(y_true, y_pred, average='weighted' , zero_division = 0 ))
        
    return  compiled_relevancy_score, rec_df

def effectivity_eval(Q, query,raw_recipe): #written by Ganyi Zhang
    rd_recipe = raw_recipe
    DQ=pd.DataFrame(Q,columns=['id'])
    token_query=word_tokenize(str(pp.preprocess(query)))
    QL=len(token_query)
    DQ['ingredient']=DQ.id.apply(lambda x: rd_recipe['ingredients'][x]) #get the ingredient of the recipes
    DQ['ingredient']=DQ.ingredient.apply(lambda x: word_tokenize(str(pp.preprocess(x)))) #get the ingredient processed
    DQ['fit']=DQ.ingredient.apply(lambda x: [n for n in x if n in token_query]) #get the ingredients that match the request
    DQ['fit']=DQ['fit'].apply(np.unique)
    DQ['number'] = DQ['fit'].str.len()# get the number of the ingredients that match the query
    DQ['percent']=DQ['number']/QL # get the propotion that fits
    DQ.drop(columns=['fit','number'], inplace=True)
    return DQ