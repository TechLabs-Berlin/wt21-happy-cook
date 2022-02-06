from pickle import FALSE, TRUE
from flask import Flask, redirect, url_for, render_template, request, session
from joblib import load
import numpy as np
import func_predict as pred 
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'

@app.route("/")
def hello_world():
    return "<p>Hello, World hey</p>"


@app.route("/<qry>/json", methods=['GET','POST'])
def query_json(qry):
    df = pd.read_csv('clean_data_for_api.csv')   #uploads dataset
    D = load('./vectorized_corpus.joblib')
    DF = load('./DF.joblib')
    N = load('./N.joblib')
    difficulty = session.get('difficulty', None) #exports difficulty level as as string.
    [model, model_score] = pred.cosine_similarity(40, qry, D , DF, N)

    d = {'id': model, 'similarity': model_score}
    DQ = pd.DataFrame(data=d)
    DQ['recipe_name']=DQ.id.apply(lambda x: df['recipe_name'][x])
    DQ['time']=DQ.id.apply(lambda x: df['total_time'][x])
    DQ['recipe_id']=DQ.id.apply(lambda x: df['recipe_id'][x])
    #added difficulty level and image_url
    DQ['Difficulty']=DQ.id.apply(lambda x: df['Difficulty'][x])
    DQ['url']=DQ.id.apply(lambda x: df['image_url'][x])
    DQ['match']=pd.Series(["{0:.2f}%".format(val * 100) for val in DQ['similarity']])
    DQ=DQ.drop(columns=['id','similarity'])
    DQ_json=DQ.to_json(orient='records', index=FALSE)  
    return DQ_json

@app.route("/tables")
def show_tables():  #this is the function to show individual recipe details.
    df = pd.read_csv('clean_data_for_api.csv')
    page_id = request.args.get("id") 
    filter = df["recipe_id"] == int(page_id)
    recipe_details = df.loc[filter,:]
    Re_json = recipe_details.to_json(orient='records', lines=TRUE, index=FALSE)  
    aha = df.to_json(orient='records', lines=TRUE, index=FALSE)  
    return Re_json

if __name__ == "__main__":
    app.run(debug=True)
