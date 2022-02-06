# Team: Data Science
********
## The Logic of the Model

Happy Cook Project developed the recipe search engine model based on the content-based recommendation approach. The rationale behind the model is that recipes with the most similar words to the user's query should be the most relevant recipes to the user's needs. We applied various natural language processing techniques to tokenize and vectorize the ingredients and cooking direction texts of 40000 recipes and then adopted the TF-IDF method to vectorize the word corpus. We then used a vector-similarity function to compute and compare the similarity scores among the recipes.

![image](https://user-images.githubusercontent.com/91828417/152676220-c625b2a0-e2a3-46d9-b097-96ff63add927.png)
*Image 1: The logic diagram of our search engine model*

## Other Features of the Model 

Given Happy Cook is a website targeting busy people, the difficulty level of recipes is also brought into the model development. The difficulty level is measured based on the duration of cooking time. By adding the difficulty level filter into the recommendation system, the model not only recommends recipes similar to the user query but also filters the recipe according to the user's preferred difficulty level.

## The Raw Dataset 

A sample of the raw dataset that was used for our model is shown below. As seen, the columns 'cooking_direction' and 'ingredients' are the most indicative of the recipe's attributes. 

![image](https://user-images.githubusercontent.com/91828417/152676746-3082afca-213e-42de-b3c8-d9e64af9a90a.png)


### Step 1: Data Cleaning

The data cleaning task was distributed among all members in the project. 

#### 1.1 Extracting cooking time and no. of steps (Ganyi, Tejesh)

As some features of the recipes are convoluted inside the 'cooking_directions' column, we have extracted the cooking time and total no. of steps into their own individual columns. This was important for the difficulty filtering feature of our web app. 

![image](https://user-images.githubusercontent.com/91828417/152678144-9daf5fa8-9bc1-4d2d-be70-3ed078af4751.png)

#### 1.2 Preparation of data for Natural Language Processing (Nisa, Jayashree)

Several functions were created in order to preprocess the recipe corpus. 
- Conversion of all words to lowercase (Nisa)
- Removal of stop words (Nisa)
- Word stemming (Nisa, Jayashree)
- Conversion of numbers to words (Nisa)
- Removal of punctuations (Nisa)

An sample of the tokenized words is shown below

![image](https://user-images.githubusercontent.com/91828417/152677455-0a3a58bd-2c6f-4258-82d3-ab4f68b9a03b.png)


#### 1.3 Used conditional statements to filter data based on difficulty criteria (Muhammad Bilal)

A new column was created to classify the recipes according to their difficulty level. We set 3 levels of difficulty: easy, medium , hard.


### Step 2: The First Version of Search Engine Model

The first version of the search engine mode was developed for our minimum viable product (MVP). A few different types were attempted, however we ended up just using the content-based similarity model.

#### 2.1 Content-Based Similarity Model (Nisa, Ganyi)

This component became the core of our machine learning model. 

The TF-IDF method was used to vectorize the word corpus of our user's query as well as the recipe collection. 
In short, TF-IDF (term frequency-inverse document frequency) is a statistical measure that evaluates how relevant a word is to a document in a collection of documents.
This is done by multiplying two metrics: how many times a word appears in a document, and the inverse document frequency of the word across a set of documents.

The equations are shown below:

>tf(t,d) = count of t in d / number of words in d

>df(t) = occurrence of t in N documents

>idf(t) = log(N/(df + 1))

>tf-idf(t, d) = tf(t, d) * log(N/(df + 1))

The function outputs a vector for each recipe in the recipe collection, with the TF-IDF scores of each term in the recipe corpus.

![image](https://user-images.githubusercontent.com/91828417/152677935-805a9350-a60a-43df-a635-cab211544552.png)

The cosine similarity function was used to calculate the similarity between each pair of vectors:

![image](https://user-images.githubusercontent.com/91828417/152678066-73e66de3-1fea-4b76-aee2-4e4a42bb8c6e.png)



#### 2.2 Other Explored Models (Nisa, Jayashree, Muhammad Bilal) (Not Implemented)

We tried exploring the implementation of "User-Based Similarity Model". However, due to the lack of time, we could not continue with this venture. The members' lack of presence and activity in this task also largely contributed to the underdevelopment of this task. Therefore, we decided to work on the content-based similarity model by tuning different parameters.

#### 2.3 Tuning of the Model (Jayashree)

Vectorizing the recipe corpus was improved by combining the ingredients and cooking_directions columns from the raw dataset. One weakness that was seen with our code is that in our query, every ingredient is weighed equally. i.e. "chicken, potatoes". Therefore, the model looks for recipes which has the greatest total frequency of both words. However, this may sometimes results in recipes which may have "potatoes" mentioned a lot of times without mentioning "chicken" at all.

After preprocessing the two columns, a combined column was created, and its words were tokenized:

`processed_text = []`

`for text in RD[“New Column”]:`

`    processed_text.append(word_tokenize(preprocess(text)))`



### Step 3: Developing the Evaluation Metrics 

Members of the group realized that there is a difference between recommendation models and search engine models. Initially we planned to use user rating as our true values to our predicted values. However, since our model does not predict ratings, the rating data is no longer relevant for our model evaluation. Unfortunately, it was highly difficult to obtain datasets which connects a query of ingredients to the clicking rate of recipes. Ideally, our team would conduct a survey of sufficient scale to gather this data. However, due to the limitations of time, we have been advised to generate our own evaluation functions.

#### 3.1 Effectivity Function (Ganyi)

The first evaluation function is called **Effectivity Function**. This function calculates the percentage of queried ingredients inside the recommended recipes outputted by the model. 

The syntax to use this function is shown below:

`percent_table = eve.effectivity_eval(Q, query,raw_recipe)`

where:
* `Q` is the list of recommended recipe indexes (of rd_recipe) outputted by the model
* `query` is the string of user query 
* `raw_recipe` is the dataframe of the recipe table 

and `percent_table` is a dataframe showing percentage values of how many ingredients in the query actually popped up in the recipes recommended by the model. 

![image](https://user-images.githubusercontent.com/91828417/152678718-b12101f8-6606-4d8b-9cb1-0a9d422352e4.png)


#### 3.2 Creating Model Dataset (Nisa) (Not Implemented)

The dataset is loaded into the variable `eval_recipe`. It consists of 57 data points. Each recipe was labeled either 1 (relevant) or 0(irrelevant) to indicate whether it is a relevant recipe to the model query. We can then do statistical analysis based on these results (i.e. recall/precision type analysis)

##### Query List:

* Query 1:  beef, salt, pepper   
* Query 2: chicken, cream      
* Query 3: noodles, chicken   
* Query 4: beef, potatoes      

##### Score metric:
* 1 = fulfils query
* 0 = does not fulfil query

![image](https://user-images.githubusercontent.com/91828417/152678418-4d8e8690-0d5d-41c4-a5f5-9e5221c8a8a6.png)

As you can see, each recipe has a score of 1 or 0 based on whether they are a relevant recipe to Query 1-4.
It is important to note that these scores were made arbitrarily based on the judgment of one DS member. Therefore we advise that the results of this evaluation to be taken with a grain of salt.

There was high bias when the model dataset was curated. Once it was used, we found that it did not provide consistent results with the Effectivity Function discussed previously. For our evaluation of the model performance, we ended up not using this evaluation method.

### Step 4: Evaluation of Model Performance (Nisa)

To show that our model works as intended, here are some samples of our model outputs, where 'ingredient_match' is the 'percent' match outputted by our Effectivity Function.

![image](https://user-images.githubusercontent.com/91828417/152678797-f51f2dcb-6629-435e-81a8-383215e3709a.png)

![image](https://user-images.githubusercontent.com/91828417/152678825-94326505-491b-4a25-84ad-1c9390d68790.png)

We also calculated the average % match between the ingredients listed in the query and ingredients listed in the top 7 recipes. Shown below are the performance of the model for some queries:

![image](https://user-images.githubusercontent.com/91828417/152678919-7013d1dd-dc20-4828-bad6-9bb10c2634b0.png)

To take away any potential bias in the model evaluation, we created a random query generator based on 20 random ingredients. 

![image](https://user-images.githubusercontent.com/91828417/152679134-c51676cd-1002-4b5d-aa7f-cc1d35fc34c7.png)

We then treated the model ouput as a classification problem, determining whether the recommended recipe is relevant(1) or irrelevant(0). We set a threshold value to the % ingredient_match to 0.75 for the recipe to be relevant to the query. The similarity score outputted by the model is also normalized so that the score ranges from 0 to 1. 

![image](https://user-images.githubusercontent.com/91828417/152679284-119b463c-165b-4510-98b9-7935b8341813.png)

Based on this criteria, we can build up true positives and false positives data for each query run. We found that ~2000 data points are necessary to produce a good resolution ROC graph, where the area under the curve indicates the performance of the model (if it works perfectly, we get ROC AUC score of 1)

![image](https://user-images.githubusercontent.com/91828417/152679369-d5d1879c-8c9a-487c-9a93-facb2f232223.png)

The equations used as the model evaluation metrics are shown below:
![image](https://user-images.githubusercontent.com/91828417/152679463-39a94bbe-fae6-4d48-926b-917b28ca4c95.png)

The evaluation result shows that model 2 provides a slightly better prediction result.
![image](https://user-images.githubusercontent.com/91828417/152679534-efe79268-479f-42fe-8db9-ff47d0d17994.png)


### Step 5: Setting up the Model API on Flask (Ganyi, Nisa)

A week was spent on creating the API for connecting our model to the backend of the web app. We used Flask to set up a local server. Two routes were created to provide the data for the results page and the details page.

