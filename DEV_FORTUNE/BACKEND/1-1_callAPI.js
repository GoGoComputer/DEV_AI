require('dotenv').config();

const OpenAI = require ('openai');



const openai = new OpenAI ({
    apiKey: process.env.OPENAI_API_KEY // defaults to process.env [OPENAI_API_KEY]
});
