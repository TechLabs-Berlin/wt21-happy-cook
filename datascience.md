datascience.md

Data Science Blog

Happy Cook Project developed the recipe recommendation model based on the content-based recommendation approach. This approach follows the logic if a user likes a certain recipe, then he/she is likely to be interested in recipes sharing similar features (Image 1). Hence, the measurement of the similarity among recipes lies in the core of the model building. We applied various natural language processing techniques to tokenize and vectorize ingredients and cooking directions of 40000 recipes and then adopted the TF-IDF method to calculate the cosine-similarity score among the recipes (Image 2&amp;3).

![](RackMultipart20220206-4-rd8i3s_html_ca20efc0abe4b59a.png) ![](RackMultipart20220206-4-rd8i3s_html_9044ea15f24f668e.png)

_Image 1: The Sample Tokenized Ingredients and Other Strings (Left) and the Similarity Score (Right)_

Given Happy Cook is a website targeting busy people, the difficulty level of recipes is also brought into the model development. The difficulty level is measured based on the duration of cooking time. By adding the difficulty level filter into the recommendation system, the model not only recommends recipes similar to the user query but also recipes adapting to the user&#39;s preferred difficulty level.

![Shape1](RackMultipart20220206-4-rd8i3s_html_9fbeed08b9d368d1.gif)

_Image 2- Recap of the Process_

![Shape2](RackMultipart20220206-4-rd8i3s_html_d94f5d4b708ed4f4.gif) ![Shape3](RackMultipart20220206-4-rd8i3s_html_7f5a33f90d6c696e.gif)

_Image 3- The Flow of the Model_

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