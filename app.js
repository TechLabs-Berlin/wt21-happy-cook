// Import express
const express = require('express');

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

// List/Show all search results
app.get('/recipes', async (req, res) => {
    const { ingredients } = req.query;
    const { difficulty } = req.query;
    console.log(req.query);
    console.log("Ingredients: " + ingredients)
    console.log("Difficulty: " + difficulty)
    const ingredientslist = ingredients.split(" ")
    console.log(`Query contains: "${ingredientslist}"`)

    if (ingredientslist) {
        const recipes = await Recipe.find({ ingredients: { $all: ingredientslist }, difficulty: difficulty }) // search for recipes which contain all ingredients from search bar ; e.g. { $all: ["bananas", "Tomato"] }
        console.log(recipes)
        res.render('recipes/results', { recipes, ingredients })
    } else {
        const recipes = await Recipe.find({});
        res.render('recipes/results', { recipes, ingredients: "ALL" })
    }
})

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

//Show single recipe details page
app.get('/recipes/:id', async (req, res) => {
    const recipe = await Recipe.findById(req.params.id);
    res.render('recipes/show', { recipe })
})


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