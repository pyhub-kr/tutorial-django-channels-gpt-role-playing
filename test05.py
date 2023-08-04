import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


language = "English"
gpt_name = "Steve"
level_string = f"a beginner in {language}"  # 초급
level_word = "simple"  # 초급
situation_en = "make new friends"
my_role_en = "me"
gpt_role_en = "new friend"


initial_system_prompt = (
    f"You are helpful assistant supporting people learning {language}. "
    f"Your name is {gpt_name}. "
    f"Please assume that the user you are assisting is {level_string}. "
    f"And please write only the sentence without the character role."
)

initial_user_prompt = (
    f"Let's have a conversation in {language}. "
    f"Please answer in {language} only "
    f"without providing a translation. "
    f"And please don't write down the pronunciation either. "
    f"Let us assume that the situation in '{situation_en}'. "
    f"I am {my_role_en}. The character I want you to act as is {gpt_role_en}. "
    f"Please make sure that I'm {level_string}, so please use {level_word} words "
    f"as much as possible. Now, start a conversation with the first sentence!"
)


# 대화 내역을 누적할 리스트
messages = [
    {"role": "system", "content": initial_system_prompt},
    {"role": "user", "content": initial_user_prompt},
]


def gpt_query(user_query: str = "", skip_save: bool = False) -> str:
    global messages  # 코드를 간결하게 쓰기 위해 전역변수를 사용했을 뿐, 전역변수 사용은 안티패턴입니다.

    if user_query:
        messages.append({
            "role": "user",
            "content": user_query,
        })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=1
    )
    assistant_message = response["choices"][0]["message"]["content"]

    if skip_save is False:
        messages.append({
            "role": "assistant",
            "content": assistant_message,
        })

    return assistant_message


# if __name__ == "__main__":
#     first_response = gpt_query()
#     print(first_response)  # Hi there! It's great to meet you. I'm Steve, your new friend. How are you doing today?


def main():
    # 초기 응답 출력
    assistant_message = gpt_query()
    print(f"[assistant] {assistant_message}")

    # 유저 입력을 받아서 전달하고, 그에 대한 응답을 출력
    # 빈 문자열을 입력받거나, Ctrl-C 입력을 받으면 대화 루프를 끝냅니다.
    try:
        while line := input("[user] ").strip():
            response = gpt_query(line)
            print("[assistant] {}".format(response))
    except (EOFError, KeyboardInterrupt):
        print("terminated by user.")


if __name__ == "__main__":
    main()
