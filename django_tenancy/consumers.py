import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SupportConsumerASync(AsyncWebsocketConsumer):
    async def connect(self):
        self.teamName = self.scope["url_route"]["kwargs"]["teamName"]
        self.user = self.scope["url_route"]["kwargs"].get("user", "AnonymousUser")
        self.room_group_name = f"chat_{self.teamName}"

        logger.debug(f"Attempting to connect for team {self.teamName}")
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
        logger.debug(f"Added to group {self.room_group_name}")

        await self.accept()
        
        logger.debug("Connection accepted")
        

    async def disconnect(self, close_code):
        logger.debug(f"Disconnecting from group {self.room_group_name}")
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]
        
        logger.debug(f"Received message: {message} from {sender}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "sender": sender}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        
        logger.debug(f"Sending message to WebSocket: {message} from {sender}")

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "sender": sender}))


