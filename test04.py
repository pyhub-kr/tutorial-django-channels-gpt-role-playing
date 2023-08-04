import os
import openai

from dotenv import load_dotenv  # python-dotenv 라이브러리 활용
load_dotenv()                   # 현재 경로의 .env 파일을 환경변수로서 로딩

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 영어 학습을 도와주는 챗봇입니다."},
        {"role": "user", "content": "대화를 나눠봅시다."},
    ],
)

print(response)

# 응답 메세지만 출력하기
print(response["choices"][0]["message"]["content"])
