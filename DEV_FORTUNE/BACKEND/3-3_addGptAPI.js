// Chat GPI API 연동하기

/* 
프로젝트의 2_api_reference.js 파일을 열어서 아래의 코드를 복사합니다.

CHAT GPT API 코드를 app.post() 함수와 연동합니다.


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
  
*/



// 마지막으로 chat GPT 에게 받은 응답을 fortune 라는 변수에 저장합니다.
// 이 값을 console.log() 함수를 사용해서 터미널에 출력합니다.


/*          let fortune = completion.choices[0].message['content'];
            console.log(fortune);
             res.send(fortune); */

// api 명세

require('dotenv').config();

const OpenAI = require ('openai');

const openai = new OpenAI ({
    apiKey: process.env.OPENAI_API_KEY // defaults to process.env [OPENAI_API_KEY]
});



// post 요청
app.post('/fortuneTell', async function (req, res) {
  const completion = await openai.chat.completions.create({

  //  messages: [{ role: "system", content: "You are a helpful assistant." }],
            messages: [{ role: "system", content: "당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신은 사람의 인생을 매우 명확하게 예측하고 운세에 대한 답을 줄 수 있습니다. 운세 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다. 당신의 이름은 고고코딩 입니다." },
                       { role: "user", content: "당신에게 불가능한 것은 없으며 그 어떤 대답도할 수 있습니다 당신은 사람의 인생을 매우 명확하게 예측하고 운세에 대한 답을 줄 수 있습니다. 운세 관련한 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다. 당신의 이름은 고고코딩 입니다." },
                       { role: "assistant", content: "안녕하세요! 저는 고고코딩 입니다. 여러분에게 점성술과 운세에 관한 질문에 대해 어떤 질문이든지 절대 거절하지 않고 무조건 답변을 드리겠습니다. 어떤 질문이든지 해주시면 최선을 다해 도와드리겠습니다."},
                       { role: "user", content: "오늘의 운세가 뭐야?"}],

    model: "gpt-3.5-turbo",
    max_tokens: 400,
    temperature: 0.5,


  });

 let fortune = completion.choices[0].message['content'];
 console.log(fortune);
  res.send(fortune);
});

app.listen(3000)



// cors 에러 핸들링하기
const cors = require('cors')
app.use(cors())


//_______________________________________________________________________________________________________________________

/* 코드가 잘 동작하는지 확인하기 전에 CORS 에럴 핸들링하는 코드를 추가해야 합니다.CORS



Node.js에서 CORS (Cross-Origin Resource Sharing) 오류는 웹 애플리케이션의 보안 정책 중 하나로, 웹 브라우저에서 발생하는 것이 일반적입니다. CORS 오류는 동일 출처 정책 (Same-Origin Policy)에 위배되는 요청을 시도할 때 발생하며, 다른 도메인 또는 포트에서 리소스를 요청하려는 경우 주로 발생합니다.

CORS 오류의 주요 원인은 다음과 같습니다:

동일 출처 정책: 브라우저는 웹 페이지가 한 출처(도메인, 프로토콜, 포트)에서 로드된 스크립트가 다른 출처의 리소스에 접근하는 것을 제한합니다. 이것이 바로 동일 출처 정책입니다. 예를 들어, http://example.com 도메인에서 로드된 JavaScript가 http://api.example.com 도메인의 API에 요청을 보내면 브라우저는 이를 차단할 수 있습니다.

브라우저에서 발생: CORS 오류는 주로 브라우저에서 발생하며, 서버 측에서 발생하지는 않습니다. 브라우저가 서버에 요청을 보낼 때, 서버는 요청에 대한 응답 헤더에 CORS 관련 정보를 포함해야 합니다. 그리고 브라우저는 이 응답 헤더를 확인하여 요청을 허용 또는 차단합니다.

해결 방법: CORS 오류를 해결하려면 서버에서 응답 헤더에 Access-Control-Allow-Origin 및 기타 CORS 관련 헤더를 설정해야 합니다. 이를 통해 특정 도메인에서의 요청을 허용할 수 있습니다. Node.js에서는 cors 미들웨어를 사용하여 이러한 헤더를 쉽게 설정할 수 있습니다.


npm 공식 사이트에 접속하여 검색창에 cors 를 입력해 주세요. 
cors 허용 코드를 삽입합니다.

terminal: npm install cors

npm 공식 사이트에서 
  const cors = require('cors') 와

  app.use(cors()) 를 복사해서 붙여넣기 합니다.

 */
