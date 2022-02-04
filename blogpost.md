## Project Description


<h3 align="center">UX</h3>
<h5 align="center">by Leticia Valladares</h5>

<p align="center">
  <a href="#Defining the problem / Possible solution">Defining the problem / Possible solution</a>  |
  <a href="#User">User Research</a>  |
  <a href="#Wireframing">Wireframing / IA / Prototyping</a>  |
  <a href="#Usability Testing">Usability Testing</a>  |
  <a href="#What’s Next">What's Next</a>
</p>

### Defining the problem / Possible solution

In the first meeting it was hard to define the problem since there were many factors to be considered when searching for a recipe. Nevertheless, in order to start with user research I started a Competitor Analysis to see what other apps were already offering and what they were missing. With this analysis, I could apply the MoSCoW method to prioritize and avoid features.

In our second meeting I could share my findings, therefore we could shape a possible solution in order to define target users, develop an appropriate Information Architecture and start with early wireframes.

**Problem**: A user has few ingredients and wants to cook something in a reduced amount of time. There are many apps that offer recipes by typing the ingredients in a search bar. However, that is not enough if the user only gets many pages with hundreds of recipes and there is just information about how long it takes to prepare the dish but there is no consideration about the time and what ingredients the user is missing.

**Solution**: A user enters ingredients or selects them and gets best recipes according to several factors (time, other users' rating, quantity of missing ingredients, diet). In order to personalize and improve this search, there will be a predicting model, which will show the best options indicating the percent of his/her/their match.

### User Research

Our first method was User Survey. After writing some questions, we compared them, selected the most relevant and uploaded them in TypeForm. Ope wrote an invite to the survey which marked a milestone: we started to share it in our social networks and reached 54 respondents.

**Target Respondents**: Users between 18 and 80, who cook (for pleasure or not), and get/buy their groceries.

The second method was User Interview. Because of time, I could only conduct one interview, which lasted 30 minutes. Even though it was only one, I could get so many insights which helped me to tune the last details for the UX artifacts.

**Personas**:

**Storyboard**:

**Scenario**:

Today Carolina works remotely in the late shift till 12 am and has only one hour lunch at 7 pm. She has already prepared pasta and chicken yesterday and have them in airtight containers in the fridge. Nevertheless, she ate pasta with chicken yesterday and doesn't want to eat this dish again.
She has other ingredients to cook another dish but doesn't want to use half of her lunch time cooking. In this situation, she remembers that HappyCook can help her to look for quicker recipe options in order to improvise another dish.
As she is using her laptop to work, she opens the webapp in a browser, checks what she has in the fridge, keeps in her mind what she wants to eat, goes back to her laptop and enters the ingredients on the search bar. She types: pasta, cheese, tomato and gets a list with the quickest recipes according to these three ingredients.
The most suitable one is "Pasta with Fresh Tomatoes and Corn" so she clicks on the recipe overview, reads what ingredients she needs and since has almost all ingredients, she decides on preparing this. It takes her 15 minutes as she had already cooked pasta yesterday, and eats it in 15 minutes. She has 30 minutes to relax and talk with her friends.

### Wireframing / IA / Prototyping

From the very first week, I had some sketches which helped me to produce wireframes. As every week we iterated our product, every week I made some changes. Sometimes there were only small changes such as creation of objects or new position of them but there were also radical ones such as redesigning all the layout since the dataset didn’t contain what was needed for one of the main original features (measure calculation).

**Wireframes**:

The **fonts** were picked with the idea of being simple, cozy, relaxed and at-home feeling.

I decided on a **flat design** so hover effect was fundamental to guide users to buttons and links and used some linear gradations to show progress.

In the early weeks I had in mind that the IA should comply with the search engine standards so the user could interact intuitively. I applied Filtered View IA in my wireframes and prototypes, and after the big change in the layout due to the lack of data, the Detailed Recipe Page was transformed into an Overview Page with Dashboard Design IA.

We decided as a team to create four main pages for the MVP: Home Page with Search Bar, Loading Page, Result Page and Overview Page.

- Home Page and Result Page - Filtered View with cards displaying results.
- Overview Page - Dashboard Design.
- Loading Page - Transition between Home Page and Results Page.

In the Home Page there are two options to go to the Result Page. To highlight the most relevant feature according to our Key Value Path: Search Bar, I used higher color contrast and positioned it in the center of the website. This made the Quick Search feature as a second and an extra option.

The Key Value Path for HappyCook is:

- (Most relevant) User types ingredient(s) in the Search Bar / (Least relevant) User selects ingredient from Quick Search.
- User gets list with recipes ordered from the most relevant to their query to the least and selects at least one of the resulting recipes.
- User sees overview of the selected recipe (ingredients, cooking directions). From this page they can go back to Results Page or go to the original recipe (external link).

**IA and Key Value Path**:

**Prototype**:
*Home Page*
*Loading Page*
*Result Page*
*Overview Page*

### Usability Testing

Due to lack of time, I had to conduct Usability Testing with a High-Fidelity Prototype. The great challenge was to replicate the functionality of a Search Bar in Figma. I could manage to use an input search bar used as a reference and explained this to the user.

https://user-images.githubusercontent.com/73216174/152541003-4a1b2477-eb22-49bc-a787-1c57d627dbdb.mp4

[Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/) from Nielsen Norman Group was my guideline. I wrote some scenarios/tasks and tested the prototype a couple of times before starting. First I asked the user to think out loud in the whole test, then I explain the first task and let the user speak and navigate. The think-out-loud technique was of great help to take note of aspects not considered in the tasks and get some suggestions.

After finishing the test, I understood that a ‘How it works Page’ was necessary. As a team we though that explaining this in the ‘About Us’ Page was enough, but we were completely wrong. That was the only task the user couldn’t finish (navigate to know how HappyCook works).The tasks related to the MVP were successfully completed, it was pretty intuitive for the user to look for recipes. Some small discrepancies between the machine learning model and prototype such as percentages with two decimals, were not pleasing to the eye.

User found out that the Inspiration Page was interesting and was looking forward to it, and was glad that registration wasn’t needed in relation to privacy.

### What’s Next:

- Redesigning ‘How it works’ Page with animates slides
- Finishing Mobile Prototype
- Finishing Dark Mode Prototype
