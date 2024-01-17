# .env file set

# 1. open ai api call

# OPENAI_API_KEY = sk-xxxxxxx

# 2. google gemini pro api call

# GOOGLE_API_KEY = AIxxxxxxx



#CHAT GPT CALL API KEY

from dotenv import load_dotenv
import os
# import openai

# `.env` 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
openai_api_key = os.getenv('OPENAI_API_KEY')

# 이제 `openai_api_key` 변수를 사용하여 OpenAI API와 연동



# GOOGLE GEMINI PRO CALL API KEY

from dotenv import load_dotenv
import os
# import openai

# `.env` 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')




