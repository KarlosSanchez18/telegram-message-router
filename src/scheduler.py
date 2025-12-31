import asyncio
from datetime import datetime

async def scheduler_loop(client):
    while True:
        await asyncio.sleep(30)
