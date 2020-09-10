# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class UserConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("users", self.channel_name)
        print(f"Se añadio {self.channel_name} a 'users'")

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)("users", self.channel_name)
        print(f"Se removio {self.channel_name} a 'users'")

    def user_users(self, event):
        ''' en el mensaje el guion bajo es interpretado como . '''
        print(f"Se recibio un evento {event} en el canal {self.channel_name}")
        # async_to_sync(self.send_json)(event)
        self.send(text_data=json.dumps(event))
    # def chat_message(self, event):
    #     message = event['message']

    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message', # esto hace que me envie a la funcion con el nombre
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
# # chat/consumers.py
# import json
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         self.send(text_data=json.dumps({
#             'message': message
#         }))
    