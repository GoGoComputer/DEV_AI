from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

import openai

def translate_to_english(korean_text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt="번역: " + korean_text,
        temperature=0.7,
        max_tokens=100,
        echo=False,
        api_key=openai_api_key
    )
    return response.choices[0].text

if __name__ == "__main__":
    while True:
        user_input = input("안녕하세요. 무엇을 도와드릴까요? ")
        english_translation = translate_to_english(user_input)
        print("ChatGPT: " + english_translation)

