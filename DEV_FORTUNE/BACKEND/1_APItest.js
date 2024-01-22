

/* 
console.log ("Hello World")


termainal: node index.js
termainal: npm init
termainal: npm install openai
terminal: npm install dotenv
termainal: npm install cors


*/

// import OpenAI from 'openai';

require('dotenv').config();

const OpenAI = require ('openai');



const openai = new OpenAI ({
    apiKey: process.env.OPENAI_API_KEY // defaults to process.env [OPENAI_API_KEY]
});


async function main () {
    const completion = await openai.chat.completions.create ({
        messages: [{ role: 'user', content: 'Say this is a test' }],
        model: 'gpt-3.5-turbo',
    });

    console.log (completion.choices);
}

main ();


/* 

will print in terminal:

- 중략 -
[
  {
    index: 0,
    message: { role: 'assistant', content: 'This is a test.' },
    logprobs: null,
    finish_reason: 'stop'
  }
] */

