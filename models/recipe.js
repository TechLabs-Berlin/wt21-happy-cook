const mongoose = require('mongoose')
const Schema = mongoose.Schema;

const RecipeSchema = new Schema({
    //tbd: check if correct 
    recipe_id: Number,
    recipe_name: String,
    aver_rate: Number,
    image_url: String,
    review_nums: Number,
    ingredients: String,
    cooking_directions: String,
    nutritions: String,
    reviews: String,
    difficulty: String //3 parts
});


// Compile model from schema ("Recipe" collection created by mongoose; Use RecipeSchema as Schema for new model)
module.exports = mongoose.model('Recipe', RecipeSchema)

