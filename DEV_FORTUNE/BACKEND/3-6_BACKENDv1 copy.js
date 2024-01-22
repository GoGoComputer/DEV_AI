// backend v1 버전입니다. v0 의 app.get 을 app.post 로 바꿔서 테스트 합니다.
//                        v0 의 res.send 를  res.json({"assistant": fortune}); 으로 바꿔서 테스트 합니다.
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
app.post('/fortuneTell', async function (req, res) {
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
  res.json({"assistant": fortune});
});

app.listen(3000)




