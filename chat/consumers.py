import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))

    def startup(self):
        text_data_json = json.loads()
        message = text_data_json["Hello! How may I help you today?"]

        self.send(text_data=json.dumps({"message": message}))