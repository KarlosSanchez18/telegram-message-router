from telethon import events
from utils import get_topic_id

def register(client, source, destination):
    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        await client.send_message(destination, event.message.text or '[Mídia]')
