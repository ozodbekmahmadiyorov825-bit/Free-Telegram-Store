import os
from datetime import datetime
from zoneinfo import ZoneInfo
from telethon import TelegramClient, functions
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION"]
TZ = os.getenv("TZ", "Asia/Tashkent")

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

async def main():
    now = datetime.now(ZoneInfo(TZ))
    clock_text = now.strftime("%H:%M")
    me = await client.get_me()
    await client(functions.account.UpdateProfileRequest(
        first_name=clock_text,
        last_name=me.last_name or ""
    ))

with client:
    client.loop.run_until_complete(main())
