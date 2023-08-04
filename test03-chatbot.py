# test03-chatbot.py

import openai

# 각자 OPENAI API KEY 지정 : 이 파일은 버전 관리에는 절대 넣지 마세요.
openai.api_key = "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"

# 챗봇 응답 생성
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"},
    ],
)

print(response["choices"][0]["message"]["content"])