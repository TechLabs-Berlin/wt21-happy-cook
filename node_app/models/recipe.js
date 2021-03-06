const mongoose = require('mongoose')
const Schema = mongoose.Schema;

const RecipeSchema = new Schema({
    //tbd: check if correct 
    recipe_id: Number,
    recipe_name: String,
    aver_rate: Number,
    image_url: String,
    review_nums: Number,
    ingredients:
        [{
            type: String,
        }],
    cooking_directions: String,
    nutritions: String,
    reviews: String,
    difficulty: {
        type: String,
        lowercase: true,
        enum: ['easy', 'normal', 'hard']
    }
});


// Compile model from schema ("Recipe" collection created by mongoose; Use RecipeSchema as Schema for new model)
module.exports = mongoose.model('Recipe', RecipeSchema)

