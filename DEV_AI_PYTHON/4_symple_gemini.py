import google.generativeai as genai

from dotenv import load_dotenv
import os
# import openai

# `.env` 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("반갑습니다")

print(response.text)


