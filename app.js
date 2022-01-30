// Import express
const express = require('express');
const axios = require('axios')
const path = require('path');

// Import Mongoose
const mongoose = require('mongoose');

const Recipe = require('./models/recipe');
const { captureRejectionSymbol } = require('events');

// Connect to Mongoose and set connection variable
mongoose.connect('mongodb://localhost:27017/happycook', {
    useNewUrlParser: true,
    // useCreateIndex: true, tbd: check why needed or not
    useUnifiedTopology: true
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
    console.log("Database connected");
});


//Initialize the app
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'))

// Configure express to handle post requests
app.use(express.urlencoded({ extended: true }))

// Render static files
app.use(express.static('public'));



//Search recipes by ingredients
app.get('/', (req, res) => {
    res.render('index')
})


// // Search Page
// app.get('/recipes/search', (req, res) => {
//     res.render('recipes/search')
// })

//// List/Show all search results
// app.get('/recipes', async (req, res) => {
//     const { ingredients } = req.query;
//     const { difficulty } = req.query;
//     console.log(req.query);
//     console.log("Ingredients: " + ingredients)
//     console.log("Difficulty: " + difficulty)
//     const ingredientslist = ingredients.split(" ")
//     console.log(`Query contains: "${ingredientslist}"`)

//     if (ingredientslist) {
//         const recipes = await Recipe.find({ ingredients: { $all: ingredientslist }, difficulty: difficulty }) // search for recipes which contain all ingredients from search bar ; e.g. { $all: ["bananas", "Tomato"] }
//         console.log(recipes)
//         res.render('recipes/results', { recipes, ingredients })
//     } else {
//         const recipes = await Recipe.find({});
//         res.render('recipes/results', { recipes, ingredients: "ALL" })
//     }
// })

// List/Show all search results (LOCAL flask server)
app.get('/recipes', async (req, res) => {
    const { ingredients } = req.query;
    const { difficulty } = req.query;
    console.log(req.query);
    console.log("Ingredients: " + ingredients)
    console.log("Difficulty: " + difficulty)
    // const ingredientslist = ingredients.split(" ")
    // console.log(`Query contains: "${ingredientslist}"`)
    console.log(`http://127.0.0.1:5000/${ingredients}/json`)
    const recipeResults = await axios.get(`http://127.0.0.1:5000/${ingredients}/json`)
    const recipes = recipeResults.data
    console.log(recipes)
    res.render('recipes/results', { recipes, ingredients })
})




// //API Testing with cryptonator API
// axios.get('https://api.cryptonator.com/api/ticker/btc-usd')
//     .then(res => {
//         console.log(res.data.ticker.price)
//     })
// 
////same as above
// const getBitconPrice = async () => {
//     const res = await axios.get('https://api.cryptonator.com/api/ticker/btc-usd')
//     console.log(res)
// }


// //Search recipes by ingredients
// app.get('/DSSEARCHTEST', (req, res) => {
//     res.render('/archiv_templates/archiv_ds-api')
// })

// // DS_API test page 
// app.get('/DSAPI', async (req, res) => {
//     const { ingredients } = req.query;
//     console.log(ingredients)
//     res.redirect(`http://127.0.0.1:5000/${ingredients}/json`)
//     //fetch(`http://127.0.0.1:5000/chicken/json`)
// })


// axios.get('http://127.0.0.1:5000/chicken/json')
//     .then(res => {
//         console.log(res.data)
//     })


// //Show all recipes (OLD)
// app.get('/recipes', async (req, res) => {
//     const recipes = await Recipe.find({});
//     res.render('recipes/index', { recipes })
// })

// Show page for creating new recipe
app.get('/recipes/new', async (req, res) => {
    res.render('recipes/new',)
})

// Create new recipe
app.post('/recipes', async (req, res) => {
    const recipe = new Recipe(req.body.recipe);
    await recipe.save();
    res.redirect(`/recipes/${recipe._id}`)
})

//Nav Bar pages
app.get('/aboutus', async (req, res) => {
    res.render('aboutus',)
})


app.get('/inspiration', async (req, res) => {
    res.render('inspiration',)
})

app.get('/gitHub', async (req, res) => {
    res.render('gitHub',)
})

app.get('/recipes/loading', async (req, res) => {
    res.render('recipes/loading',)
})

app.get('/recipes/results', async (req, res) => {
    res.render('recipes/results',)
})

app.get('/recipes/recipe', async (req, res) => {
    res.render('recipes/recipe',)
})


//Testing of flask API 
// axios.get('http://127.0.0.1:5000/tables?id=237610')
//     .then(res => {
//         console.log(res.data.ingredients)
//     })


//Show single recipe details page (LOCAL flask Server) 
app.get('/recipes/:id', async (req, res) => {
    const recipeID = req.params.id;
    console.log(recipeID);

    const recipeDetails = await axios.get(`http://127.0.0.1:5000/tables?id=${recipeID}`)
    const recipe = recipeDetails.data
    console.log(recipe)

    const all_ingredients = recipe.ingredients.split("^")
    console.log(all_ingredients)

    const all_cooking_directions = recipe.cooking_directions.split("^")
    console.log(all_cooking_directions)


    res.render('recipes/recipe', { recipe, all_ingredients, all_cooking_directions })
})


// //Show single recipe details page (LOCAL MongoDB Server // OLD Version)
// app.get('/recipes/:id', async (req, res) => {
//     const recipe = await Recipe.findById(req.params.id); // e.g. "61d5fc6688e42aae66f94a5f"
//     console.log(recipe)
//     res.render('recipes/recipe', { recipe })
// })


// //MAKE new recipe:
// app.get('/makerecipe', async (req, res) => {
//     const recipe = new Recipe({
//         recipe_id: 653542,
//         recipe_name: "Tomato Soup recipe v4", cooking_directions: "Cut tomatos and cook", ingredients: "Tomato", difficulty: "easy"
//     });
//     await recipe.save();
//     res.send(recipe);
// })


//Launch app to listen to specified port
app.listen(3000, () => {
    console.log('Serving on port 3000')
})