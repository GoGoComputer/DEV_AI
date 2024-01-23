// 프런트엔드에 채팅 데이터 누적하기
// 변수 생성

let userMessages = [];
let assistantMessages = [];


async function sendMessage () {

// 사용자 메시지 입력
const messageInput = document.getElementById('messageInput');
const message = messageInput.value;

// 사용자 메시지 화면에 출력
const userBubble = document.createElement('div');
userBubble.className = 'chat-bubble user-bubble';
userBubble.textContent = message;
document.getElementById("fortuneResponse").appendChild(userBubble);

// userMessages 배열에 사용자 메시지 저장
userMessages.push(messageInput.value);

// 입력 필드 초기화
messageInput.value = '';

// 백엔드에 메시지 전송하고 응답을 받아옵니다.

try {
    const response = await axios.post('http://localhost:3000/fortuneTell', {
        mathod: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },


        // userMessages 라는 이름 key 에 userMessages 의 값 value assistanMessages 라는 key 에
    // assistantMessages 의 값 value 를 넣은 자바스크립트 객체를 만들어 JSON.stringify() 함수의 파라미터로 전달합니다.
    body: JSON.stringify({
        userMessages: userMessages,
        assistantMessages: assistantMessages,
    })
});
   

    if (!response.ok) {
        throw new Error('Resquest failed with status' + response.status);
    }

    const data = await response.json();
    console.log('Response:', data.assistant);

    // 백엔드 응답을 화면에 출력합니다. chat GPT 응답을 말풍선에 응답 출력
    const botBubble = document.createElement('div');
    botBubble.className = 'chat-bubble bot-bubble';
    botBubble.textContent = data.assistant;
    document.getElementByid('fortuneResponse').appendChild(botBubble);




    // assistantMessages 배열에 chat GPT의 응답 저장
    assistantMessages.push(data.assistant);

} catch (error) {
    console.error('Error:', error);
 }
}

/* JSON.stringify() 함수는 프론트와 백엔드 간 JSON 형태의 데이트를 주고 받을 때 사용합니다.
자바스크립트의 값이나 객체를 JSON 형태의 문자열로 변환합니다. */

