import json
from dataclasses import asdict
from logging import getLogger

from channels.generic.websocket import AsyncWebsocketConsumer

from core.controllers.client import ClientController

logger = getLogger('client')


class AsyncChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_controller = None

    async def connect(self):
        logger.info('START CONNECTION')

        try:
            self.client_controller = await ClientController.get_by_headers(self.scope['headers'])
            logger.info(f'CONNECTED: {self.client_controller.client} {self.channel_name}')
        except ClientController.SessionNotFound:
            logger.info(f'NOT CONNECTED: {self.scope}')
            await self.close(403, 'Session not found')

        await self.accept()

    async def disconnect(self, close_code):
        await self.client_controller.delete_window()
        logger.info('DISCONNECTED')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.client_controller.update_window(**message)

        await self.send(text_data=json.dumps({
            'message': [
                asdict(render_info)
                async for render_info in self.client_controller.get_render_info()
            ]
        }))
