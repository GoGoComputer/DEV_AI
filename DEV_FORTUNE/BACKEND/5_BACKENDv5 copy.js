// backend v2 버전입니다. chat GPT 로 코드를 수정했습니다.


const express = require('express'); 
const cors = require('cors');
const app = express(); 
app.use(cors());
app.use(express.json()); // JSON 요청 본문을 처리하기 위해 필요합니다.

require('dotenv').config();
const OpenAI = require('openai');
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.post('/fortuneTell', async function (req, res) {
    const completion = await openai.chat.completions.create({



//____________________아래 쪽 내용은 v1 과 동일___________________________________________________________________________________________________
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
//_______________위쪽 코드는 v1 과 동일________________________________________________________________________________________________________
  let fortune = completion.choices[0].message.content; // 수정됨
    console.log(fortune);
    res.json({"assistant": fortune});
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});



