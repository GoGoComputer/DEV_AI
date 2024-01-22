/* express API 서버 만들기
terminal: npm install express

go to https://www.npmjs.com/package/express



*/

// GET 요청에 HELLO WORLD 출력하기

const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World')
})

app.listen(3000)