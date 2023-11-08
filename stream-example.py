# test03-chatbot.py

from dotenv import load_dotenv
load_dotenv()

import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"},
    ],
    stream=True,
)

for message in response:
    content = message["choices"][0]["delta"].get("content", "")
    print(content, end="", flush=True)

