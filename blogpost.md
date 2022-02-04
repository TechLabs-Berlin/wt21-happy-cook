<h2 align="left">Project Description</h2>

<h2 align="left">UX</h2>
<h5 align="left">by Leticia Valladares</h5>

<h5 align="left">
  <a href="#strategy">Strategy</a>  ||
  <a href="#scope">Scope</a>  ||
  <a href="#structure">Structure</a>  ||
  <a href="#skeleton">Skeleton</a>  ||
  <a href="#surface">Surface</a>  ||
  <a href="#testing">Testing</a>  ||
  <a href="#future">Future</a>
</h5>

&nbsp;
&nbsp;
&nbsp;

### Strategy
#### Defining the problem / Possible solution

&nbsp;

In the first meeting it was hard to define the problem since there were many factors to be considered when searching for a recipe. Nevertheless, in order to start with user research I started a Competitor Analysis to see what other apps were already offering and what they were missing. With this analysis, I could apply the MoSCoW method to prioritize and avoid features.

In our second meeting I could share my findings, therefore we could shape a possible solution in order to define target users, develop an appropriate Information Architecture and start with early wireframes.

**Problem**: A user has few ingredients and wants to cook something in a reduced amount of time. There are many apps that offer recipes by typing the ingredients in a search bar. However, that is not enough if the user only gets many pages with hundreds of recipes and there is just information about how long it takes to prepare the dish but there is no consideration about the time and what ingredients the user is missing.

**Solution**: A user enters ingredients or selects them and gets best recipes according to several factors (time, other users' rating, quantity of missing ingredients, diet). In order to personalize and improve this search, there will be a predicting model, which will show the best options indicating the percent of his/her/their match.

&nbsp;
&nbsp;
&nbsp;

### Scope
#### User Research

&nbsp;

Our first method for User Research was **User Survey**. After writing some questions, we compared them, selected the most relevant and uploaded them in TypeForm. We started to share it in our social networks and reached 54 respondents.

**Target Respondents**: Users between 18 and 80, who cook (for pleasure or not), and get/buy their groceries.

Based on quantitative results from the survey, we selected the three main features of HappyCook.

&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152563596-675a679c-022c-4154-b7ab-4fc4edcb3c89.png>
</p>

[See Typeform Survey](https://7v2689hvz4u.typeform.com/to/dmVKDJJY)
[See further insights](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#35fce534a2ea4a72963b688e17867e8c)

Our second method was **User Interview**. Because of time, I could only conduct one interview, which lasted 30 minutes. Even though it was only one, I could get so many insights which helped me to tune the last details for the UX artifacts.

[See interview transcription](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#7234de53c77944a0afd3087156c4068e)
[See interview insights](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#ab3df716e5ee498cb04573c98bd1a135)

&nbsp;

**Personas**:
&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548480-43253d3a-855c-4839-a111-2bf2815defd0.png>

&nbsp;
&nbsp;

<img src=https://user-images.githubusercontent.com/73216174/152548489-a59cc90a-ed45-4728-9dd2-5bc0deab658c.png>
</p>

&nbsp;
&nbsp;
&nbsp;

**Storyboard**:
&nbsp;

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548501-a20571ae-9370-45c4-a966-df2e5fa24e32.png>
  </p>

[See full storyboard](https://www.canva.com/design/DAEyjVsXhTo/view)

&nbsp;

**Scenario**:
Today Carolina works remotely in the late shift till 12 am and has only one hour lunch at 7 pm. She has already prepared pasta and chicken yesterday and have them in airtight containers in the fridge. Nevertheless, she ate pasta with chicken yesterday and doesn't want to eat this dish again.
She has other ingredients to cook another dish but doesn't want to use half of her lunch time cooking. In this situation, she remembers that HappyCook can help her to look for quicker recipe options in order to improvise another dish.
As she is using her laptop to work, she opens the webapp in a browser, checks what she has in the fridge, keeps in her mind what she wants to eat, goes back to her laptop and enters the ingredients on the search bar. She types: pasta, cheese, tomato and gets a list with the quickest recipes according to these three ingredients.
The most suitable one is "Pasta with Fresh Tomatoes and Corn" so she clicks on the recipe overview, reads what ingredients she needs and since has almost all ingredients, she decides on preparing this. It takes her 15 minutes as she had already cooked pasta yesterday, and eats it in 15 minutes. She has 30 minutes to relax and talk with her friends.

&nbsp;
&nbsp;
&nbsp;

### Structure
#### Wireframing / Information Architecture

&nbsp;

From the very first week, I had some sketches which helped me to produce wireframes. As every week we iterated our product, every week I made some changes. Sometimes there were only small changes such as creation of objects or new position of them but there were also radical ones such as redesigning all the layout since the dataset didn’t contain what was needed for one of the main original features (measure calculation).

&nbsp;

**Wireframes**:

<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152548652-c984e2ca-f71f-4ecb-9c87-5efcda274e74.png>

&nbsp;
&nbsp;

<img src=https://user-images.githubusercontent.com/73216174/152549870-7722b24a-0dd7-403d-9281-9b3b3f16ca19.jpg>
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
<img src=https://user-images.githubusercontent.com/73216174/152549846-6e155094-634d-4d1f-9b80-f5c7b9d040d1.png>
</p>

&nbsp;
&nbsp;
&nbsp;

### Skeleton
#### Prototyping

**Prototype**:
*Home Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556811-2cff0253-ead1-44b4-990c-6e638834471c.png>
</p>

&nbsp;
&nbsp;

*Loading Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556831-cc4b181f-c072-4425-a839-dd712972ad75.png>
</p>

&nbsp;
&nbsp;

*Result Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556856-c7c9e862-85a1-4722-b493-09f47c60f150.png>
</p>

&nbsp;
&nbsp;

*Overview Page*
<p align="center">
<img src=https://user-images.githubusercontent.com/73216174/152556834-86409f20-b942-4087-baee-2a0c3e7d37af.png>
</p>

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

[See Usability Test Report](https://www.notion.so/happycook/HappyCook-UX-b945b4438e014fefbae45cf0bac6adeb#be40bd27cb3249f7b20659f28287a5a1)

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
<img src=https://user-images.githubusercontent.com/73216174/152559598-87ee1874-4e6b-4fed-95f9-a727d6d2796a.png>
</p>
