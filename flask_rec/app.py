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


@app.route("/search", methods=["POST", "GET"])  #this gets us to the search page
def search():
    if request.method == "POST":
        query = request.form["nm"]
        
        #sample buttons for the difficulty level
        if request.form['submit_button'] == 'Easy':
            difficulty = "Easy"
        elif request.form['submit_button'] == 'Medium':
            difficulty = "Medium"# do something else
        elif request.form['submit_button'] == 'Difficult':
            difficulty = "Difficult"# do something else
        else:
            pass # unknown
        #difficulty = request.form["easy"]
        session['difficulty'] = difficulty
        return redirect(url_for("query", qry=query ))
    else:
        return render_template("login.html")
        

@app.route("/<qry>", methods=['GET','POST'])
def query(qry):
    df = pd.read_csv('clean_data_for_api.csv')   #uploads dataset
    df=df[df['Difficulty']=='Easy']
    D = load('vectorized_corpus.joblib')
    DF = load('DF.joblib')
    N = load('N.joblib')
    difficulty = session.get('difficulty', None) #exports difficulty level as as string.
    [model, model_score] = pred.cosine_similarity(6, qry, D , DF, N)

    d = {'id': model, 'similarity': model_score}
    DQ = pd.DataFrame(data=d)

      #the filter keeps return error, could you please edit it? Thanks (it does work in jupyitor notebook)#
    #if difficulty == 'Easy':
        #results=data[data['Difficulty']=='Easy']
   # elif difficulty == 'Medium':    
        #results=data[data['Difficulty']=='Medium']
    #elif difficulty == 'Difficult':  
        #results=data[data['Difficulty']=='Difficult']
   # else:
       # results=None#
    
    DQ['recipe_name']=DQ.id.apply(lambda x: df['recipe_name'][x])
    DQ['time']=DQ.id.apply(lambda x: df['total_time'][x])
    DQ['recipe_id']=DQ.id.apply(lambda x: df['recipe_id'][x])
    DQ['match']=pd.Series(["{0:.2f}%".format(val * 100) for val in DQ['similarity']])
    DQ=DQ.drop(columns=['id','similarity'])

    if request.method == "POST":  #I still need to somehow make a button/link beside every recipe. But assume that you are clicking the recipe id 12345
        if request.form['recipe_button'] == '87211':
            recip_id = "87211"
            session['recip_id'] = recip_id #exporting the recipe id 
            # without this button, you can change the id on the link : http://localhost:5000/tables?id=87211#
            return redirect(url_for("show_tables", id=recip_id )) #this indicates that the page is now rerouted to the show_tables function
    else:
        return render_template('alltables.html',tables=[DQ.to_html()],  #if nothing is clicked, the page will keep showing all tables
    titles = [ 'easy recipe'])

@app.route("/<qry>/json", methods=['GET','POST'])
def query_json(qry):
    df = pd.read_csv('clean_data_for_api.csv')   #uploads dataset
    D = load('./vectorized_corpus.joblib')
    DF = load('./DF.joblib')
    N = load('./N.joblib')
    difficulty = session.get('difficulty', None) #exports difficulty level as as string.
    [model, model_score] = pred.cosine_similarity(25, qry, D , DF, N)

    d = {'id': model, 'similarity': model_score}
    DQ = pd.DataFrame(data=d)
    DQ['recipe_name']=DQ.id.apply(lambda x: df['recipe_name'][x])
    DQ['time']=DQ.id.apply(lambda x: df['total_time'][x])
    DQ['recipe_id']=DQ.id.apply(lambda x: df['recipe_id'][x])
    DQ['match']=pd.Series(["{0:.2f}%".format(val * 100) for val in DQ['similarity']])
    DQ=DQ.drop(columns=['id','similarity'])
    DQ_json=DQ.to_json(orient='records', index=FALSE)  
    return DQ_json

@app.route("/tables")
def show_tables():  #this is the function to show individual recipe details.
    df = pd.read_csv('clean_data_for_api.csv')
    page_id = request.args.get("id") # 123
    filter = df["recipe_id"] == int(page_id)
    recipe_details = df.loc[filter,:]
    Re_json = recipe_details.to_json(orient='records', lines=TRUE, index=FALSE)  
    aha = df.to_json(orient='records', lines=TRUE, index=FALSE)  
    return Re_json

if __name__ == "__main__":
    app.run(debug=True)
