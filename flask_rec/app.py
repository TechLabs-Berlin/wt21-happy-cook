from flask import Flask, redirect, url_for, render_template, request
from joblib import load
import numpy as np
import func_predict as pred 

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        query = request.form["nm"]
        return redirect(url_for("query", qry=query))
    else:
        return render_template("login.html")
        

@app.route("/<qry>")
def query(qry):
    D = load('./vectorized_corpus.joblib')  #the vectorized recipe collection
    DF = load('./DF.joblib')   # the document frequency of each term
    N = load('./N.joblib')   # the length of the total recipe collection
    [model, model_score] = pred.cosine_similarity(6, qry, D , DF, N)

    return f"<h1>{qry} {model} {model_score} </h1>"

if __name__ == "__main__":
    app.run(debug=True)
