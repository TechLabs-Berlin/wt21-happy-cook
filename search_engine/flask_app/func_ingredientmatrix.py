
def ingredientmatrix(url_raw_data_recipe):
    
    #Function created by Nisa Ulumuddin on 13/12/2021
    #This function creates a matrix where the headers are: recipe_id [ a list of all ingredients in the dataset]
    #The matrix values will be consist of 0 or 1 values, depending on whether the ingredient is present in the recipe or not. 
    #To run the function, the user will need to insert the url for the raw recipe data. 
    
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer

    #load recipe dataset
    rd_recipe = pd.read_csv(url_raw_data_recipe)


    df_ingred = rd_recipe[["recipe_id", "ingredients"]].copy()  # select only relevant columns
    df_ingred['ingredients'] = [x.replace('^', ',') for x in df_ingred['ingredients']] # change ^ sep to , sep

    vect = CountVectorizer() # instantiate the vectorizer
    ingred_dtm = vect.fit_transform(df_ingred["ingredients"]) #learn data vocab and put into matrix
    ingred_matrix = pd.DataFrame(ingred_dtm.toarray(), columns=vect.get_feature_names()) #visualize in DataFrame table
    ingred_matrix = ingred_matrix[ingred_matrix.columns.drop(list(ingred_matrix.filter(regex='\d+')))] #delete columns with digits
    ingred_matrix.insert(0, column='recipe_id', value=df_ingred["recipe_id"]) #add recipe_id as the first column
    return ingred_matrix
