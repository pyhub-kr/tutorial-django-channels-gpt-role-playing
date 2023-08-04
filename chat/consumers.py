# chat/consumers.py
from typing import List

from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AbstractUser

from chat.models import GptMessage, RolePlayingRoom


class RolePlayingRoomConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpt_messages: List[GptMessage] = []

    # 웹소켓 연결 요청을 받으면 호출됩니다.
    def connect(self):
        room = self.get_room()
        if room is None:
            self.close()
        else:
            self.accept()

            self.gpt_messages = room.get_initial_messages()
            # TODO: self._gpt_messages 기반으로 gpt api 호출.
            print(f"{self.gpt_messages=}")

    def get_room(self) -> RolePlayingRoom | None:
        user: AbstractUser = self.scope["user"]
        room_pk = self.scope["url_route"]["kwargs"]["room_pk"]
        room: RolePlayingRoom = None

        if user.is_authenticated:
            try:
                room = RolePlayingRoom.objects.get(pk=room_pk, user=user)
            except RolePlayingRoom.DoesNotExist:
                pass

        return room

    # 웹소켓 유저로부터 메시지를 받으면 receive_json 메서드가 호출됩니다.
    def receive_json(self, content, **kwargs):
        # gpt-3.5-turbo API 호출을 통해 응답을 생성하고,
        # self.send_json을 통해 응답 메시지를 웹소켓 유저에게 전송합니다.
        # self.send_json({ 임의의_사전_데이터 })
        self.send_json(content)  # Echo 응답.
