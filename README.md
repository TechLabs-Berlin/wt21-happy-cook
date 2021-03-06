&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/149679461-b22ff91c-a52f-49b2-9553-f8712dcd74b0.png>
</p>

<p align="center">
<img src=https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white>
<img src=https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54>
<img src=https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white>
<img src=https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white>
</p>

&nbsp;

<h5 align="center">
  <a href="#About">About</a>  |
  <a href="#Prototype">Prototype</a>  |
  <a href="#Setup">Setup</a>  |
  <a href="#Running">Run</a>  |
  <a href="#Authors">Authors</a>
</h5>

&nbsp;

## About

HappyCook is Recipe Search Engine designed for busy people. Users can input their available ingredients or select them to search for their favorite recipes according to several factors such as ingredients, time, and difficulty. Using our powerful algorithms, HappyCook suggests a list with the most relevant recipes to the least ones providing key data and an overview of each recipe.

&nbsp;

## Prototype

https://user-images.githubusercontent.com/73216174/152697069-a8305a60-b67f-49f6-b196-1de575ad121a.mp4

&nbsp;

## Setup
##### Requirements: python, nodeJS

### Express app
> Use the package manager [npm](https://npmjs.com/) to install the dependencies

1. From the top-level directory: `wt21-happy-cook`

2. Change to folder: `$ cd node_app`

3. Run following commands to install express and dependencies:

 ```sh
 npm install
 ```

### Flask server
> for installation

1. Go to the directory: `wt21-happy-cook/python_app/flask_app`

2. Install python: $ pip install python  or  $ pip3 install python

3. Install flask (for more info <a href="https://flask.palletsprojects.com/en/2.0.x/installation/">click here</a>)

4. Run the following commands to install all dependencies:

  ```sh
  $ pip install numpy
  ```

  ```sh
  $ pip install joblib
  ```

  ```sh
  $ pip install pandas
  ```

  ```sh
  $ pip install num2words
  ```

  ```sh
  $ pip install ???user -U nltk
  ```

  
  (for more information on nltk [click here](https://www.nltk.org/install.html))

  Note: If you find any ImportError messages, continue to install missing dependencies.

&nbsp;

## Running
**to start up the flask server**:

1. Go to the directory: `wt21-happy-cook/python_app/flask_app`

2. Make sure that you are in the virtual environment (venv).
  If you are not, reactivate the environment (see link <a href=???https://flask.palletsprojects.com/en/2.0.x/installation/???>click here</a>)

3. Run the following commands:

  ```sh
  $ export FLASK_APP=app
  ```

  ```sh
  $ flask run
  ```

**to start up express** run command:

1. Go to the directory: `wt21-happy-cook/node_app`

2. Run the following commands:

 ```sh
 $ node app.js
 ```

&nbsp;

## Authors
Data Science:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Nisa Ulumuddin](https://github.com/nisaulumuddin) &nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Ganyi Zhang](https://github.com/Yii67) &nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Jayashree Prabhakaran](https://github.com/JayashreePrabhakaran) &nbsp;

WD Frontend:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Nikola Jelavi??](https://github.com/NikolaJelavic) &nbsp;

WD Backend:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Abiraam Kantharajah](https://github.com/akrava25) &nbsp;

User Experience:&nbsp;&nbsp; [Leticia Valladares](https://github.com/lavf) &nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Ajimati Opeyemi](https://github.com/ope1521)
