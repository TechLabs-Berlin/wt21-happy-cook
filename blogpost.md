<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/149679461-b22ff91c-a52f-49b2-9553-f8712dcd74b0.png>
</p>

<h5 align="center">
  <a href="#Description">Project Description</a>  |
  <a href="#UX">User Experience</a>  |
  <a href="#DS">Data Science</a>  |
  <a href="#WD-Backend">WD Backend</a>  |
  <a href="#WD-Frontend">WD Frontend</a>
</h5>

&nbsp;

## Description

HappyCook is Recipe Search Engine designed for busy people. Users can input their available ingredients or select them to search for their favorite recipes according to several factors such as ingredients, time, and difficulty. Using our powerful algorithms, HappyCook suggests a list with the most relevant recipes to the least ones providing key data and an overview of each recipe.

During the project, a team of 2 UX/UI designers, 2 web developers, and 3 data scientists actively applied and deepened their knowledge, acquired during the TechLabs Academic Phase. Using common tools from every discipline, the project team developed a functioning, responsive, and user-friendly prototype. As in every project, there were challenges. In our case, we were faced with a lack of data, experience, and time. Despite that, we were able to agree on a weekly MVP to find agreeable solutions to every challenge in conjunction with our mentor, Kathryn Rough.

We are happy to bring an interdisciplinary project of this scope to life within a 10-week period while having fun and respecting each other's needs. Thank you for having us!

&nbsp;
&nbsp;
&nbsp;

## UX
#### by [Leticia](https://github.com/lavf)

<h5 align="left">
  || &nbsp; <a href="#strategy">Strategy</a> &nbsp; ||
  &nbsp; <a href="#scope">Scope</a> &nbsp; ||
  &nbsp; <a href="#structure">Structure</a> &nbsp; ||
  &nbsp; <a href="#skeleton">Skeleton</a> &nbsp; ||
  &nbsp; <a href="#surface">Surface</a> &nbsp; ||
  &nbsp; <a href="#testing">Testing</a> &nbsp; ||
  &nbsp; <a href="#future">Future</a> &nbsp; ||
</h5>

&nbsp;
&nbsp;
&nbsp;

### Strategy
#### Defining the problem / Possible solution

In the first meeting it was hard to define the problem since there were many factors to be considered when searching for a recipe. Nevertheless, in order to start with user research I started a Competitor Analysis to see what other apps were already offering and what they were missing. With this analysis, I could apply the MoSCoW method to prioritize and avoid features.

In our second meeting I could share my findings, therefore we could shape a possible solution in order to define target users, develop an appropriate Information Architecture and start with early wireframes.

**Problem**: A user has few ingredients and wants to cook something in a reduced amount of time. There are many apps that offer recipes by typing the ingredients in a search bar. However, that is not enough if the user only gets many pages with hundreds of recipes and there is just information about how long it takes to prepare the dish but there is no consideration about the time and what ingredients the user is missing.

**Solution**: A user enters ingredients or selects them and gets best recipes according to several factors (time, other users' rating, quantity of missing ingredients, diet). In order to personalize and improve this search, there will be a predicting model, which will show the best options indicating the percent of his/her/their match.

&nbsp;
&nbsp;
&nbsp;

### Scope
#### User Research

Our first method for User Research was **User Survey**. After writing some questions, we compared them, selected the most relevant and uploaded them in TypeForm. We started to share it in our social networks and reached 54 respondents.

**Target Respondents**: Users between 18 and 80, who cook (for pleasure or not), and get/buy their groceries.

Based on quantitative results from the survey, we selected the three main features of HappyCook.

&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152563596-675a679c-022c-4154-b7ab-4fc4edcb3c89.png width="600" />
</p>

[> See Typeform survey](https://7v2689hvz4u.typeform.com/to/dmVKDJJY)
&nbsp;

[> See further insights](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#35fce534a2ea4a72963b688e17867e8c)

&nbsp;

Our second method was **User Interview**. Because of time, I could only conduct one interview, which lasted 30 minutes. Even though it was only one, I could get so many insights which helped me to tune the last details for the UX artifacts.

[> See interview transcription](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#7234de53c77944a0afd3087156c4068e)
&nbsp;

[> See interview insights](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#ab3df716e5ee498cb04573c98bd1a135)

&nbsp;

**Personas**:
&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548480-43253d3a-855c-4839-a111-2bf2815defd0.png width="600" />
</p>

&nbsp;
&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548489-a59cc90a-ed45-4728-9dd2-5bc0deab658c.png width="600" />
</p>

&nbsp;
&nbsp;
&nbsp;

**Storyboard**:
&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548501-a20571ae-9370-45c4-a966-df2e5fa24e32.png width="600" />
  </p>

[> See full storyboard](https://www.canva.com/design/DAEyjVsXhTo/view)

&nbsp;

**Scenario**:
&nbsp;

Today Carolina works remotely in the late shift till 12 am and has only one hour lunch at 7 pm. She has already prepared pasta and chicken yesterday and have them in airtight containers in the fridge. Nevertheless, she ate pasta with chicken yesterday and doesn't want to eat this dish again.
She has other ingredients to cook another dish but doesn't want to use half of her lunch time cooking. In this situation, she remembers that HappyCook can help her to look for quicker recipe options in order to improvise another dish.
As she is using her laptop to work, she opens the webapp in a browser, checks what she has in the fridge, keeps in her mind what she wants to eat, goes back to her laptop and enters the ingredients on the search bar. She types: pasta, cheese, tomato and gets a list with the quickest recipes according to these three ingredients.
The most suitable one is "Pasta with Fresh Tomatoes and Corn" so she clicks on the recipe overview, reads what ingredients she needs and since has almost all ingredients, she decides on preparing this. It takes her 15 minutes as she had already cooked pasta yesterday, and eats it in 15 minutes. She has 30 minutes to relax and talk with her friends.

&nbsp;
&nbsp;
&nbsp;

### Structure
#### Wireframing / Information Architecture

From the very first week, I had some sketches which helped me to produce wireframes. As every week we iterated our product, every week I made some changes. Sometimes there were only small changes such as creation of objects or new position of them but there were also radical ones such as redesigning all the layout since the dataset didn’t contain what was needed for one of the main original features (measure calculation).

&nbsp;

**Wireframes**:

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548652-c984e2ca-f71f-4ecb-9c87-5efcda274e74.png width="600" />
</p>
&nbsp;
&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152549870-7722b24a-0dd7-403d-9281-9b3b3f16ca19.jpg width="600" />
  </p>

&nbsp;

In the early weeks I had in mind that the IA should comply with the search engine standards so the user could interact intuitively. I applied Filtered View IA in my wireframes and prototypes, and after the big change in the layout due to the lack of data, the Detailed Recipe Page was transformed into an Overview Page with Dashboard Design IA.

&nbsp;

We decided as a team to create four main pages for the MVP: *Home Page* with Search Bar, *Loading Page*, *Result Page* and *Overview Page*.

- Home Page and Result Page - Filtered View with cards displaying results.
- Overview Page - Dashboard Design.
- Loading Page - Transition between Home Page and Results Page.

In the Home Page there are two options to go to the Result Page. To highlight the most relevant feature according to our Key Value Path: Search Bar, I used higher color contrast and positioned it in the center of the website. This made the Quick Search feature as a second and an extra option.

&nbsp;

The **Key Value** Path for HappyCook is:

- (Most relevant) User types ingredient(s) in the Search Bar / (Least relevant) User selects ingredient from Quick Search.
- User gets list with recipes ordered from the most relevant to their query to the least and selects at least one of the resulting recipes.
- User sees overview of the selected recipe (ingredients, cooking directions). From this page they can go back to Results Page or go to the original recipe (external link).

&nbsp;

**IA and Key Value Path**:

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152549846-6e155094-634d-4d1f-9b80-f5c7b9d040d1.png width="900" />
</p>

&nbsp;
&nbsp;
&nbsp;

### Skeleton
#### Prototyping

*Home Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556811-2cff0253-ead1-44b4-990c-6e638834471c.png width="900" />
</p>

&nbsp;
&nbsp;

*Loading Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556831-cc4b181f-c072-4425-a839-dd712972ad75.png width="900" />
</p>

&nbsp;
&nbsp;

*Result Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556856-c7c9e862-85a1-4722-b493-09f47c60f150.png width="900" />
</p>

&nbsp;
&nbsp;

*Overview Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556834-86409f20-b942-4087-baee-2a0c3e7d37af.png width="900" />
</p>

[> See High-Fidelity Desktop Prototype](https://www.figma.com/proto/cFAruddFG2PtB5Wa9CKp0R/HappyCook_Prototype?scaling=min-zoom&page-id=0%3A1&starting-point-node-id=350%3A575&node-id=877%3A7503)
&nbsp;

[> See High-Fidelity Mobile Prototype](https://www.figma.com/proto/cFAruddFG2PtB5Wa9CKp0R/HappyCook_Prototype?node-id=1206%3A8429&scaling=scale-down&page-id=1206%3A7749&starting-point-node-id=1206%3A8429)

&nbsp;
&nbsp;
&nbsp;

### Surface
#### Design

Regarding colors, fonts and images, the dataset contained the images so we couldn’t use high quality pictures. Nevertheless, I could create a logo, played with color palettes and fonts.

&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548756-671534da-d404-471f-9b79-73af28ddaf8f.svg>
</p>

&nbsp;

The **logo** transmits both concepts of HappyCook: Happiness and Cooking. Even it’s not animated, the flames and smiling pot give a glance of emotion and action.

&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152549822-30bcad1a-68e9-466c-9da1-6b75db1dc84b.svg>
</p>

&nbsp;

The **color palette** was took from the logo and the home background image. I didn’t want to use the standard white as background color since the dataset pictures didn’t have good quality and white background highlights the images. Colors were more in the dark palette side, but keeping in mind contrast (monochrome test). I kept red variations as the main colors since red was the main original color in the project pitch slides.

I used some **rules for colors** to keep everything logic and structured, more than pretty, that is to say: there is only one color for all hover effects, one for titles without link, one for text without link, one for activated links, and another one for not-activated links. I applied the same for buttons.

&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548703-31b58c85-71f7-4420-ab4e-0b9c1643a70a.png>
</p>

&nbsp;

The **fonts** were selected with the idea of being simple, cozy, relaxed and at-home feeling.

I decided on a **flat design** so hover effect was fundamental to guide users to buttons and links and used some linear gradations to show progress.

&nbsp;
&nbsp;
&nbsp;

### Testing
#### Usability Testing

Due to lack of time, I had to conduct **Usability Testing** with a High-Fidelity Prototype. The great challenge was to replicate the functionality of a Search Bar in Figma. I could manage to use an input search bar used as a reference and explained this to the user.

&nbsp;

https://user-images.githubusercontent.com/73216174/152541003-4a1b2477-eb22-49bc-a787-1c57d627dbdb.mp4

&nbsp;

[Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/) from Nielsen Norman Group was my guideline. I wrote some scenarios/tasks and tested the prototype a couple of times before starting. First I asked the user to think out loud in the whole test, then I explain the first task and let the user speak and navigate. The think-out-loud technique was of great help to take note of aspects not considered in the tasks and get some suggestions.

After finishing the test, I understood that a ‘How it works Page’ was necessary. As a team we though that explaining this in the ‘About Us’ Page was enough, but we were completely wrong. That was the only task the user couldn’t finish (navigate to know how HappyCook works).The tasks related to the MVP were successfully completed, it was pretty intuitive for the user to look for recipes. Some small discrepancies between the machine learning model and prototype such as percentages with two decimals, were not pleasing to the eye.

User found out that the Inspiration Page was interesting and was looking forward to it, and was glad that registration wasn’t needed in relation to privacy.

[> See Usability Test Report](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#be40bd27cb3249f7b20659f28287a5a1)

&nbsp;
&nbsp;
&nbsp;

### Future
#### What’s Next:

- Redesigning ‘How it works’ Page with animated slides
- Finishing Mobile Prototype
- Finishing Dark Mode Prototype

&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152688862-f727fddc-4e20-4c34-9f67-a04eb57720c0.png width="900" />
</p>

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## DS
#### by [Nisa](https://github.com/nisaulumuddin), [Ganyi](https://github.com/Yii67) and [Jayashree](https://github.com/JayashreePrabhakaran)

&nbsp;

### The Logic of the Model

Happy Cook Project developed the recipe search engine model based on the content-based recommendation approach. The rationale behind the model is that recipes with the most similar words to the user's query should be the most relevant recipes to the user's needs. We applied various natural language processing techniques to tokenize and vectorize the ingredients and cooking direction texts of 40000 recipes and then adopted the TF-IDF method to vectorize the word corpus. We then used a vector-similarity function to compute and compare the similarity scores among the recipes.

![image](https://user-images.githubusercontent.com/91828417/152676220-c625b2a0-e2a3-46d9-b097-96ff63add927.png)
*Image 1: The logic diagram of our search engine model*

### Other Features of the Model

Given Happy Cook is a website targeting busy people, the difficulty level of recipes is also brought into the model development. The difficulty level is measured based on the duration of cooking time. By adding the difficulty level filter into the recommendation system, the model not only recommends recipes similar to the user query but also filters the recipe according to the user's preferred difficulty level.

### The Raw Dataset

A sample of the raw dataset that was used for our model is shown below. As seen, the columns 'cooking_direction' and 'ingredients' are the most indicative of the recipe's attributes.

![image](https://user-images.githubusercontent.com/91828417/152676746-3082afca-213e-42de-b3c8-d9e64af9a90a.png)


#### Step 1: Data Cleaning

The data cleaning task was distributed among all members in the project.

##### 1.1 Extracting cooking time and no. of steps (Ganyi, Tejesh)

As some features of the recipes are convoluted inside the 'cooking_directions' column, we have extracted the cooking time and total no. of steps into their own individual columns. This was important for the difficulty filtering feature of our web app.

![image](https://user-images.githubusercontent.com/91828417/152678144-9daf5fa8-9bc1-4d2d-be70-3ed078af4751.png)

##### 1.2 Preparation of data for Natural Language Processing (Nisa, Jayashree)

Several functions were created in order to preprocess the recipe corpus.
- Conversion of all words to lowercase (Nisa)
- Removal of stop words (Nisa)
- Word stemming (Nisa, Jayashree)
- Conversion of numbers to words (Nisa)
- Removal of punctuations (Nisa)

An sample of the tokenized words is shown below

![image](https://user-images.githubusercontent.com/91828417/152677455-0a3a58bd-2c6f-4258-82d3-ab4f68b9a03b.png)


##### 1.3 Used conditional statements to filter data based on difficulty criteria (Muhammad Bilal)

A new column was created to classify the recipes according to their difficulty level. We set 3 levels of difficulty: easy, medium , hard.


#### Step 2: The First Version of Search Engine Model

The first version of the search engine mode was developed for our minimum viable product (MVP). A few different types were attempted, however we ended up just using the content-based similarity model.

##### 2.1 Content-Based Similarity Model (Nisa, Ganyi)

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



##### 2.2 Other Explored Models (Nisa, Jayashree, Muhammad Bilal) (Not Implemented)

We tried exploring the implementation of "User-Based Similarity Model". However, due to the lack of time, we could not continue with this venture. The members' lack of presence and activity in this task also largely contributed to the underdevelopment of this task. Therefore, we decided to work on the content-based similarity model by tuning different parameters.

##### 2.3 Tuning of the Model (Jayashree)

Vectorizing the recipe corpus was improved by combining the ingredients and cooking_directions columns from the raw dataset. One weakness that was seen with our code is that in our query, every ingredient is weighed equally. i.e. "chicken, potatoes". Therefore, the model looks for recipes which has the greatest total frequency of both words. However, this may sometimes results in recipes which may have "potatoes" mentioned a lot of times without mentioning "chicken" at all.

To give more weight to the ingredients, we explored vectorizing both the 'cooking_directions' and 'ingredients' texts to represent the recipe vector.
After preprocessing the two columns, a combined column was created, and its words were tokenized:

`processed_text = []`

`for text in RD[“New Column”]:`

`    processed_text.append(word_tokenize(preprocess(text)))`



#### Step 3: Developing the Evaluation Metrics

Members of the group realized that there is a difference between recommendation models and search engine models. Initially we planned to use user rating as our true values to our predicted values. However, since our model does not predict ratings, the rating data is no longer relevant for our model evaluation. Unfortunately, it was highly difficult to obtain datasets which connects a query of ingredients to the clicking rate of recipes. Ideally, our team would conduct a survey of sufficient scale to gather this data. However, due to the limitations of time, we have been advised to generate our own evaluation functions.

##### 3.1 Effectivity Function (Ganyi)

The first evaluation function is called **Effectivity Function**. This function calculates the percentage of queried ingredients inside the recommended recipes outputted by the model.

The syntax to use this function is shown below:

`percent_table = eve.effectivity_eval(Q, query,raw_recipe)`

where:
* `Q` is the list of recommended recipe indexes (of rd_recipe) outputted by the model
* `query` is the string of user query
* `raw_recipe` is the dataframe of the recipe table

and `percent_table` is a dataframe showing percentage values of how many ingredients in the query actually popped up in the recipes recommended by the model.

![image](https://user-images.githubusercontent.com/91828417/152678718-b12101f8-6606-4d8b-9cb1-0a9d422352e4.png)


##### 3.2 Creating Model Dataset (Nisa) (Not Implemented)

The dataset is loaded into the variable `eval_recipe`. It consists of 57 data points. Each recipe was labeled either 1 (relevant) or 0(irrelevant) to indicate whether it is a relevant recipe to the model query. We can then do statistical analysis based on these results (i.e. recall/precision type analysis)

###### Query List:

* Query 1:  beef, salt, pepper   
* Query 2: chicken, cream      
* Query 3: noodles, chicken   
* Query 4: beef, potatoes      

###### Score metric:
* 1 = fulfils query
* 0 = does not fulfil query

![image](https://user-images.githubusercontent.com/91828417/152678418-4d8e8690-0d5d-41c4-a5f5-9e5221c8a8a6.png)

As you can see, each recipe has a score of 1 or 0 based on whether they are a relevant recipe to Query 1-4.
It is important to note that these scores were made arbitrarily based on the judgment of one DS member. Therefore we advise that the results of this evaluation to be taken with a grain of salt.

There was high bias when the model dataset was curated. Once it was used, we found that it did not provide consistent results with the Effectivity Function discussed previously. For our evaluation of the model performance, we ended up not using this evaluation method.

#### Step 4: Evaluation of Model Performance (Nisa)

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

We evaluated two model versions.

![image](https://user-images.githubusercontent.com/91828417/152680845-03398a2b-d5a7-45dd-be8f-e9c0fe64a4ae.png)


Our table shows the average ROC AUC (for 2000 data points) and average % match (for top 7 recipes) based on 10 runs.

![image](https://user-images.githubusercontent.com/91828417/152679534-efe79268-479f-42fe-8db9-ff47d0d17994.png)

It indicates that tuning of the model by vectorizing a combined 'ingredients' and 'cooking_directions' column improves the performance of the model slightly. As future work, we need to figure out a better strategy to ensure that the recipes are listed in descending order of their % ingredient match score.

#### Step 5: Setting up the Model API on Flask (Ganyi, Nisa)

A week was spent on creating the API for connecting our model to the backend of the web app. We used Flask to set up a local server. Two routes were created to provide the data for the results page and the details page.

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## WD-Backend
#### by [Abiraam](https://github.com/akrava25)

The development of the backend of happy cooks was characterized by ups and downs. Overall, the backend was developed in an agile way using smaller packages and goals, which led to weekly endproducts. Initially, there was no explicit coordination with the frontend or the datascience track, which led to some code not being needed in the final MVP (see section "technical journey > Part 4).


### Technical journey:
The creation of the backend is divided into the following 5 phases:

#### 1. Finish academic phase
At the start of the project, there was a major confusion for me regarding my progress of the academic part of the Techlab course. Online I was shown that I had already completed 94% of my theoretical part. Practically, however, the last 6% was a majority of the backend learning. This resulted in me lacking the knowledge to even have an approach on where and how to set up a backend for the website. The first step for me was to finish the last 6% of the academic part.

#### 2. Development of the first MVP without frontend and datascience
At this stage, my goal was to create an extremely simple version of the website. Basically, this should enable the following: Show me recipes for 1 or more ingredients.

I realized this with node.js (incl. npm packages), MongoDB and mongoose.

In the following you can see a few images of this phase:

Search page:  

<p align="center">
<img src=https://user-images.githubusercontent.com/91902360/152676122-f0ead7bb-08a6-46d0-ba18-2dc9566b3b08.png>
</p>


Results page:

<p align="center">
<img src=https://user-images.githubusercontent.com/91902360/152676192-1ae22d45-56c9-4769-8b28-aceb824ed44e.png>
</p>


Details page:

<p align="center">
<img src=https://user-images.githubusercontent.com/91902360/152676231-42ad6c25-23a8-4280-b5ac-cb755e79157e.png>
</p>


#### 3. Connecting backend to frontend
In the third phase, my backend was to be connected to the frontend. Nikola and I regularly exchanged feedback for this. Here, various problems occurred, such as "search bar was no longer centered", "some links in the navigation bar did not work". We were able to correct these problems with both more and less effort.

#### 4. Connecting website with datascience algorithm
The goal at this stage was to link Datascience's algorithm to the website. My original idea of having all the recipes uploaded to MongoDB and then integrating DataScience's algorithm or python code into my node.js was quickly dropped after a conversation with the trackleads from the web development team. Instead, datascience and I agreed on the following API structure:

![API_structure](https://user-images.githubusercontent.com/91902360/152676403-bc0cf475-6a9d-4f53-90db-8c8d6adc1ea5.png)

As with the frontend and backend work, several alignments were necessary here as well, so that the right data could be connected via the right endpoints.
In the end, we were able to look back on a solid and functioning connection between the website and the database.

#### 5. MVP finalization
In this phase, we fixed the last issues and finished the last details.
For example:
- difficulty filtering
- correct image URLs for the recipes
- show matching score in details page
\
\
\
I am very happy with the result of our website. Even though setting up the MongoDB server was useless in retrospect, I still found it necessary to have a better understanding of the whole system. Only with frequent coordination and great communication within the team it was possible for us to create such a MVP.

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;

## WD-Frontend
##### by [Nikola](https://github.com/NikolaJelavic)

While creating Happy cook web site Bootstrap5 was used, since it is HTML, CSS & JS Library that focuses on simplifying the development.
It was useful for responsiveness, buttons and modals.

Also, Bootstrap is having flexbox grids to build layouts of shapes and sizes thanks to a twelve-column system and six default-responsive tiers.
It was planned that website is responsive, but, while connecting frontend and backend, some frontend things had to be removed/refactored, so only desktop version was done.

JavaScript was used for creating “to the top” button and tags inside of input field, while writing ingredients.

Also JS was used for creating slider for choosing ingredients.
