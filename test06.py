import os
import sys
from io import BytesIO
from tempfile import NamedTemporaryFile
from gtts import gTTS
import pygame

from test05 import gpt_query, messages


def play_file(file_path: str):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # 오디오 파일이 재생되는 동안 기다립니다.
    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()


def say(message: str, lang: str):
    io = BytesIO()

    # 생성된 음성파일을 파일 객체에 저장합니다.
    # 장고 View에서 수행되었다면, HttpResponse 객체에 음성 파일을 바로 저장하실 수 있습니다.
    gTTS(message, lang=lang).write_to_fp(io)

    if "win" in sys.platform:
        with NamedTemporaryFile(delete=False) as f:
            f.write(io.getvalue())
            f.close()
            play_file(f.name)
            os.remove(f.name)
    else:
        with NamedTemporaryFile() as f:
            f.write(io.getvalue())
            play_file(f.name)


def main():
    # 초기 응답 출력
    assistant_message = gpt_query()
    print(f"[assistant] {assistant_message}")

    try:
        while line := input("[user] ").strip():
            if line == "!say":  # ADDED
                say(messages[-1]["content"], "en")
            else:
                response = gpt_query(line)
                print("[assistant] {}".format(response))
    except (EOFError, KeyboardInterrupt):
        print("terminated by user.")


if __name__ == "__main__":
    main()
