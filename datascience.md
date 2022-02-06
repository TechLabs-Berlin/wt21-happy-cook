# Team: Data Science
********
## The Logic of the Model

Happy Cook Project developed the recipe search engine model based on the content-based recommendation approach. The rationale behind the model is that recipes with the most similar words to the user's query should be the most relevant recipes to the user's needs. We applied various natural language processing techniques to tokenize and vectorize the ingredients and cooking direction texts of 40000 recipes and then adopted the TF-IDF method to vectorize the word corpus. We then used a vector-similarity function to compute and compare the similarity scores among the recipes.

![image](https://user-images.githubusercontent.com/91828417/152676220-c625b2a0-e2a3-46d9-b097-96ff63add927.png)
*Image 1: The logic diagram of our search engine model*

## Other Features of the Model 

Given Happy Cook is a website targeting busy people, the difficulty level of recipes is also brought into the model development. The difficulty level is measured based on the duration of cooking time. By adding the difficulty level filter into the recommendation system, the model not only recommends recipes similar to the user query but also filters the recipe according to the user's preferred difficulty level.

### Step 1: Data Cleaning

#### 1.1 Extracting cooking time and no. of steps 

#### 1.2 Preparation of data for Natural Language Processing

#### 1.3 Used conditional statements to filter data based on difficulty criteria 

### Step 2: The First Version of Search Engine Model

#### 2.1 Content-Based Similarity Model 

#### 2.2 Other Explored Models

### Step 3: Developing the Evaluation Metrics 

#### 3.1 Effectivity Function

#### 3.2 Creating Model Dataset (Excluded)

### Step 4: Evaluation of Model Performance

### Step 5: Setting up the Model API on Flask 

Following this logic, two models were developed and evaluated (Image 2). Model evaluation was based on two evaluation metrics: precision/recall evaluation metric and an effectivity evaluation function. The ROC curve was plotted by treating the similarity score as the predicted results and the effectivity evaluation result as the true results (Image 4&amp; 5). The evaluation result shows that model 2 provides a slightly better prediction result (Table 1).

![](RackMultipart20220206-4-rd8i3s_html_c22fc8e294cba27.png)

_Image 4: Illustration of the effectivity evaluation result and similarity score._

![](RackMultipart20220206-4-rd8i3s_html_b05deed110e5c3a.png)

_Image 5: The ROC Curve_

| **Model Iterations** | **Avg ROC Area Under the Curve**** (top 2000 rec) **|** Avg Average Ingredient Match****(top 7 rec)** |
| --- | --- | --- |
| 1 | 0.74 | 0.41 |
| 2 | 0.79 | 0.50 |

_Table 1: The Model Result_
