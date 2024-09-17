import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """
        Метод вызывается при подключении клиента по веб-сокету.
        Мы добавляем пользователя в группу с именем 'chat_group' и принимаем соединение.
        """
        self.room_name = 'chat_group'  # Имя группы для чата (можно сделать уникальным для каждого чата)
        self.room_group_name = f'chat_{self.room_name}'

        # Присоединяемся к группе чата
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """
        Метод вызывается при отключении клиента по веб-сокету.
        Мы удаляем пользователя из группы и уведомляем остальных участников о его выходе.
        """
        # Удаляем клиента из группы
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Отправляем сообщение всем остальным участникам чата
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'Пользователь {self.channel_name} вышел из чата.'
            }
        )

    def receive(self, text_data):
        """
        Метод вызывается при получении сообщения от клиента по веб-сокету.
        Сообщение отправляется обратно всем участникам группы.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправляем сообщение всем участникам группы
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        """
        Метод вызывается при получении сообщения от группы.
        Отправляем сообщение клиенту.
        """
        message = event['message']

        # Отправляем сообщение клиенту
        self.send(text_data=json.dumps({
            'message': message
        }))
