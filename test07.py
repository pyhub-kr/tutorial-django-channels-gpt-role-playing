from test05 import level_word, gpt_query, messages
from test06 import say


RECOMMEND_PROMPT = (
    f"Can you please provide me an {level_word} example "
    f"of how to respond to the last sentence "
    f"in this situation, without providing a translation "
    f"and any introductory phrases or sentences."
)


def main():
    # 초기 응답 출력
    assistant_message = gpt_query()
    print(f"[assistant] {assistant_message}")

    try:
        while line := input("[user] ").strip():
            if line == "!recommend":
                # 추천표현 요청은 대화내역에 저장하지 않겠습니다.
                recommended_message = gpt_query(RECOMMEND_PROMPT, skip_save=True)
                print("추천 표현:", recommended_message)
            elif line == "!say":  # ADDED
                say(messages[-1]["content"], "en")
            else:
                response = gpt_query(line)
                print("[assistant] {}".format(response))
    except (EOFError, KeyboardInterrupt):
        print("terminated by user.")


if __name__ == "__main__":
    main()
