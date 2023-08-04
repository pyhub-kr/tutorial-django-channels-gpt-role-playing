# chat/consumers.py

from channels.generic.websocket import JsonWebsocketConsumer


class RolePlayingRoomConsumer(JsonWebsocketConsumer):

    # 웹소켓 연결 요청을 받으면 호출됩니다.
    # def connect(self):
        # self.accept()  # 웹소켓 연결 요청 수락합니다. 거부는 self.close()

    # 웹소켓 유저로부터 메시지를 받으면 receive_json 메서드가 호출됩니다.
    def receive_json(self, content, **kwargs):
        # gpt-3.5-turbo API 호출을 통해 응답을 생성하고,
        # self.send_json을 통해 응답 메시지를 웹소켓 유저에게 전송합니다.
        # self.send_json({ 임의의_사전_데이터 })
        self.send_json(content)  # Echo 응답.
