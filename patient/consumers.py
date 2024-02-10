import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import uuid

class chan (AsyncWebsocketConsumer):

    async def connect (self):

        if self.scope.get('user').pk is None:
            await self.close()
        else:


            await self.accept()





            self.room_group_name=str(self.scope.get('user').pk)##

            await self.channel_layer.group_add( self.room_group_name, self.channel_name)

            await self.send(text_data=json.dumps({
                'type': 'connection_established',
                'message': 'yes'}))


    async def disconnect(self, close_code):
        await   self.channel_layer.group_discard(str(self.scope.get('user').pk), self.channel_name)


    async def receive(self, text_data):


       text_data_json=json.loads(text_data)

       message=text_data_json['message']


       await self.channel_layer.group_send(str(25),{
       'type':'chat_message',
        'message':message

       })





    async def chat_message(self,event):
        message = event["message"]


        await self.send(text_data=json.dumps( message))

