Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## This function needs to be paired with the juypter notebook similarityfunc 
def evaluation(Q):
    DQ=pd.DataFrame(Q,columns=['id'])
    token_query=word_tokenize(str(preprocess(query)))
    QL=len(token_query)
    DQ['ingredient']=DQ.id.apply(lambda x: rd_recipe['ingredients'][x])
    #get the ingredient of the recipes
    DQ['ingredient']=DQ.ingredient.apply(lambda x: word_tokenize(str(preprocess(x))))
    #get the ingredient processed
    DQ['fit']=DQ.ingredient.apply(lambda x: [n for n in x if n in token_query]) 	#get the ingredients that match the request
    DQ['fit']=DQ['fit'].apply(np.unique)
    DQ['number'] = DQ['fit'].str.len()
    # get the number of the ingredients that match the query
    DQ['percent']=DQ['number']/QL
    # get the propotion that fits
    DQ.drop(columns=['fit','number'], inplace=True)
    return DQ