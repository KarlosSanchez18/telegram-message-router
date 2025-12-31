from telethon import TelegramClient
import asyncio
from config import API_ID, API_HASH, SESSION_NAME
from router import register
from scheduler import scheduler_loop

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    await client.start()
    asyncio.create_task(scheduler_loop(client))
    await client.run_until_disconnected()

asyncio.run(main())
