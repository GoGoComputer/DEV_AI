/* 

api 명세 확인하기
go to https://platform.openai.com/docs/api-reference/chat/create

copy code and paste it into vscode


api 명세 설명
    API 명세(API Specification)란, 소프트웨어 개발에서 다른 소프트웨어 컴포넌트나 서비스와 상호 작용하기 위한 인터페이스 및 규칙을 정의하는 문서 또는 설명서를 말합니다. API는 "Application Programming Interface"의 약자로, 다른 소프트웨어와의 상호 작용을 위한 표준화된 방법을 제공합니다.

    API 명세는 다음과 같은 내용을 포함할 수 있습니다:

    엔드포인트 및 URL: 다른 소프트웨어가 API를 호출하기 위해 사용해야 하는 URL 주소 및 엔드포인트 명세를 제공합니다.

    HTTP 메서드: API 요청을 보내기 위해 사용해야 하는 HTTP 메서드 (GET, POST, PUT, DELETE 등) 및 각 메서드의 용도를 설명합니다.

    매개변수 및 요청 본문: API 요청에 필요한 매개변수와 요청 본문의 형식과 내용을 정의합니다.

    응답 형식: API 응답의 형식과 내용을 설명합니다. 이에는 상태 코드, 데이터 형식(JSON, XML 등), 에러 처리 방법 등이 포함될 수 있습니다.

    인증 및 권한: API를 사용하기 위한 인증 방법과 권한에 관한 정보를 제공합니다.

    예제: 실제 API 요청 및 응답의 예제를 포함하여 개발자가 API를 쉽게 이해하고 사용할 수 있도록 돕습니다.

    API 명세는 다른 개발자나 개발팀과의 협업을 위한 중요한 도구이며, 서로 다른 시스템 간에 데이터나 서비스를 공유하고 통합하는 데 사용됩니다. 명확하고 자세한 API 명세는 소프트웨어 개발 프로세스를 단순화하고 오류를 방지하는 데 도움이 됩니다.

 */


// call api

// require('dotenv').config();

/* const OpenAI = require ('openai');

const openai = new OpenAI ({
    apiKey: process.env.OPENAI_API_KEY // defaults to process.env [OPENAI_API_KEY]
});

 */
// api 명세


require('dotenv').config();

const OpenAI = require ('openai');

const openai = new OpenAI ({
    apiKey: process.env.OPENAI_API_KEY // defaults to process.env [OPENAI_API_KEY]
});

async function main() {
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

  console.log(completion.choices[0].message['content']);
}

main();


