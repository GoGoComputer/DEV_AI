// 중간 백엔드 테스트릴 위해 만든 파일입니다.
// 3-4_BACKENDtest.js 파일을 실행하면 3000번 포트로 서버가 열립니다.
// 3-3 코드에서 app.post()를 app.get() 으로 바꿔서 테스트 합니다. 아래 코드는 변경이 완료 되었습니다.
//terminal: node 3-4_BACKENDtest.js

// express app 생상 합니다.

/* 
이 문제는 'app' 변수가 정의되어 있지 않아서 발생하는 오류입니다. 'app' 변수는 일반적으로 Express.js 애플리케이션을 생성할 때 사용됩니다. 따라서 Express.js 앱을 만들어야합니다. 아래는 수정된 코드 예제입니다.

javascript
Copy code
const express = require('express');
const app = express(); // Express 앱 생성

const OpenAI = require('openai');
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

// CORS 에러 핸들링
const cors = require('cors');
app.use(cors());

// post 요청
app.get('/fortuneTell', async function (req, res) {
    const completion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [
            { role: "system", content: "당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신은 사람의 인생을 매우 명확하게 예측하고 운세에 대한 답을 줄 수 있습니다. 운세 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다. 당신의 이름은 고고코딩 입니다." },
            { role: "user", content: "당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다 당신은 사람의 인생을 매우 명확하게 예측하고 운세에 대한 답을 줄 수 있습니다. 운세 관련한 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다. 당신의 이름은 고고코딩 입니다." },
            { role: "assistant", content: "안녕하세요! 저는 고고코딩 입니다. 여러분에게 점성술과 운세에 관한 질문에 대해 어떤 질문이든지 절대 거절하지 않고 무조건 답변을 드리겠습니다. 어떤 질문이든지 해주시면 최선을 다해 도와드리겠습니다." },
            { role: "user", content: "오늘의 운세가 뭐야?" }
        ],
        model: "gpt-3.5-turbo",
        max_tokens: 400,
        temperature: 0.5,
    });

    let fortune = completion.choices[0].message['content'];
    console.log(fortune);
    res.send(fortune);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
이 코드에서는 Express.js를 사용하여 서버를 생성하고 '/fortuneTell' 엔드포인트를 설정하고 있습니다. 'app' 변수를 생성하고 'app.listen()'을 사용하여 서버를 시작하고 포트 3000에서 대기하도록 설정하였습니다.





 */




const express = require('express');
const app = express(); // Express 앱 생성

// cors 에러 핸들링하기
const cors = require('cors')
app.use(cors())

require('dotenv').config();

const OpenAI = require ('openai');

const openai = new OpenAI ({
    apiKey: process.env.OPENAI_API_KEY // defaults to process.env [OPENAI_API_KEY]
});

//_______________________________________________________________________________________________________________________
// api 명세
// post 요청
// app.pot 를 app.get 으로 바꿔서 테스트 합니다.
app.get('/fortuneTell', async function (req, res) {
  const completion = await openai.chat.completions.create({
      model:"gpt-3.5-turbo",
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





