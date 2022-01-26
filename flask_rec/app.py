from flask import Flask, redirect, url_for, render_template, request, session
from joblib import load
import numpy as np
import func_predict as pred 
import pandas as pd

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
        else:
            pass # unknown
        #difficulty = request.form["easy"]
        session['difficulty'] = difficulty
        return redirect(url_for("query", qry=query ))
    else:
        return render_template("login.html")
        

@app.route("/<qry>", methods=['GET','POST'])
def query(qry):
    data = pd.read_csv('sample_recipe_table.csv')  #uploads dataset
    D = load('./vectorized_corpus.joblib')
    DF = load('./DF.joblib')
    N = load('./N.joblib')
    difficulty = session.get('difficulty', None) #exports difficulty level as as string.
    [model, model_score] = pred.cosine_similarity(6, qry, D , DF, N)
    
    top_list = data.iloc[0:3,:]   #we need to only show the recipes which are in the top 6 
    
    if request.method == "POST":  #I still need to somehow make a button/link beside every recipe. But assume that you are clicking the recipe id 12345
        if request.form['recipe_button'] == '12345':
            recip_id = "12345"
            session['recip_id'] = recip_id #exporting the recipe id 
            # without this button, you can change the id on the link : http://localhost:5000/tables?id=12345#
            return redirect(url_for("show_tables", id=recip_id )) #this indicates that the page is now rerouted to the show_tables function
    else:
        return render_template('alltables.html',tables=[top_list.to_html()],  #if nothing is clicked, the page will keep showing all tables
    titles = [ 'easy recipe'])



@app.route("/tables")
def show_tables():  #this is the function to show individual recipe details.
    data = pd.read_csv('sample_recipe_table.csv')
    recip_id = int(session.get('recip_id', None))
    filter = data.recipe_id == recip_id
    recipe_details = data.loc[filter, :]
    
    return render_template('view.html',tables=[recipe_details.to_html()],
    titles = [ 'easy recipe'])



if __name__ == "__main__":
    app.run(debug=True)
