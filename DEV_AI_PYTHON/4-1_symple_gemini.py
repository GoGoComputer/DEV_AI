# pip3 install google-generativeai

import google.generativeai as genai

from dotenv import load_dotenv
import os
import requests


# `.env` 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


# 사용자에게 인사말을 입력받기
greeting = input("인사말을 입력하세요: ")

# 인사말을 사용하여 텍스트 생성하기
response = model.generate_content(greeting)

# 텍스트 출력하기
print(response.text)


# 질문과 답변을 제미나이 API에 보내기
def send_answer_to_gemini_api(question, answer):
    from dotenv import load_dotenv
    load_dotenv()

    headers = {
        "Authorization": "Bearer " + os.getenv("GOOGLE_API_KEY"),
    }
    data = {
        "question": question,
        "answer": {
            "text": answer,
        },
    }
    response = requests.post("https://api.generative.ai/v1/answers", headers=headers, data=data)
    if response.status_code == 200:
        print("답변을 제미나이 API에 성공적으로 전송했습니다.")
    else:
        print("답변을 제미나이 API에 전송하는 데 실패했습니다.")


# 질문과 답변을 제미나이 API에 보내기
question = input("질문을 해주세요: ")
answer = response.text
print(f"제미나이 답변: {response.json()['answer']}")
send_answer_to_gemini_api(question, answer)


