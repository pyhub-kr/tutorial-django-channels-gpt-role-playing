# test03-fix-grammar.py

import openai

# 각자 OPENAI API KEY 지정 : 이 파일은 버전 관리에는 절대 넣지 마세요.
openai.api_key = "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"

# 텍스트 생성 혹은 문서 요약
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="""
Fix grammar errors:
- I is a boy
- You is a girl""".strip(),
)

print(response.choices[0].text.strip())
