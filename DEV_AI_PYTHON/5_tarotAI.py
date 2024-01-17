# 타로카드 랜덤으로 3개 뽑고 geminie pro 에게 질문하는 프로그램
# 20240118 DEV IN WSL UBUNTU
# pip3 install google-generativeai

# run python file in Dedicated terminal



# 절차 1 카드 3장 뽑아서 보여주는 절차

import random

# 타로카드 목록 정의
cards = {
    1: "Fool",
    2: "Magician",
    3: "High Priestess",
    4: "Empress",
    5: "Emperor",
    6: "Hierophant",
    7: "Lovers",
    8: "Chariot",
    9: "Strength",
    10: "Hermit",
    11: "Wheel of Fortune",
    12: "Justice",
    13: "Hanged Man",
    14: "Death",
    15: "Temperance",
    16: "Devil",
    17: "Tower",
    18: "Star",
    19: "Moon",
    20: "Sun",
    21: "Judgement",
    22: "World",
    23: "Ace of Wands",
    24: "Two of Wands",
    25: "Three of Wands",
    26: "Four of Wands",
    27: "Five of Wands",
    28: "Six of Wands",
    29: "Seven of Wands",
    30: "Eight of Wands",
    31: "Nine of Wands",
    32: "Ten of Wands",
    33: "Page of Wands",
    34: "Knight of Wands",
    35: "Queen of Wands",
    36: "King of Wands",
    37: "Ace of Cups",
    38: "Two of Cups",
    39: "Three of Cups",
    40: "Four of Cups",
    41: "Five of Cups",
    42: "Six of Cups",
    43: "Seven of Cups",
    44: "Eight of Cups",
    45: "Nine of Cups",
    46: "Ten of Cups",
    47: "Page of Cups",
    48: "Knight of Cups",
    49: "Queen of Cups",
    50: "King of Cups",
    51: "Ace of Swords",
    52: "Two of Swords",
    53: "Three of Swords",
    54: "Four of Swords",
    55: "Five of Swords",
    56: "Six of Swords",
    57: "Seven of Swords",
    58: "Eight of Swords",
    59: "Nine of Swords",
    60: "Ten of Swords",
    61: "Page of Swords",
    62: "Knight of Swords",
    63: "Queen of Swords",
    64: "King of Swords",
    65: "Ace of Pentacles",
    66: "Two of Pentacles",
    67: "Three of Pentacles",
    68: "Four of Pentacles",
    69: "Five of Pentacles",
    70: "Six of Pentacles",
    71: "Seven of Pentacles",
    72: "Eight of Pentacles",
    73: "Nine of Pentacles",
    74: "Ten of Pentacles",
    75: "Page of Pentacles",
    76: "Knight of Pentacles",
    77: "Queen of Pentacles",
    78: "King of Pentacles",
}

# 3개의 카드 랜덤하게 뽑기
selected_cards = random.sample(cards.keys(), 3)

# 뽑힌 카드 이름 목록 만들기
card_names = [cards[card] for card in selected_cards]


# 뽑힌 카드 이름 출력
""" print("뽑힌 카드:")
for card_name in card_names:
   # print(f"{card_name}")
   print(*card_names, sep=' ') 이 주석 활성화시 카드가 각각 3 줄로 표시
   api 엔 마지막 1장만 전달되는 문제 있음"""
   
print("뽑힌 카드:", *card_names, sep=' ')
    

# 절차 2 print 뽑힌 카드 api 로 보내는 절차
     
     
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

response = model.generate_content(f"- {card_names} 이 3가지 타로카드 자세히 해석해줘")
                                                    # 이 3가지 ... 부터 내용 변경해도 됨.
                                                    
print(response.text)

# end