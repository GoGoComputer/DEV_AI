/* express API 서버 만들기

*/

/* 
const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World')
})

app.listen(3000) */

//_______________________________________________________________________________________

/* 
post 방식으로 변경 하는 방법


1. express 공식 웹사이트
  https://expressjs.com/ko/
  안내서 -> 라우팅 
  라우트 메소드 아래 app.post() 찾기 그리고 복사


          // POST method route
          app.post('/', function (req, res) {
            res.send('POST request to the homepage');
          });

2. app.get() -> app.post() 로 변경
  */



/* const express = require('express')
const app = express()

// POST method route
app.post('/', function (req, res) {
  res.send('POST request to the homepage');
});


app.listen(3000) */

//_______________________________________________________________________________________

/* POST 방식은 데이터를 HTTP 메시지의 본문 (body)에 담아서 전송합니다.
  이 데이터는 프론트엔드에서 서버로 보내게 되는데 이를 백엔드에서 읽으려면
  추가로 설정할 것이 입습니다 
  
  EXPRESS 공식 웹사이트 검색창에 RES.BODY 를 검색해서 나오는
  내용을 참고해서 코드를 추가해 줍니다.


          app.use(express.json()) // for parsing application/json
          app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded
  파싱 코드를 복사하여 app.post() 위에 붙여넣기 합니다.
  */

  const express = require('express')
  const app = express()

  // POST 요청을 받을 수 있게 만들기
  app.use(express.json()) // for parsing application/json
  app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

  // post 요청 받기 받아서 hello world 출력하기

  app.post('/fortuneTell', function (req, res) {
    res.send('POST request to the homepage');
  });

  app.listen(3000)
  
