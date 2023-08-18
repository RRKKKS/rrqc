import asyncio
from pyrogram import Client,filters,enums,idle
from config import *
from asyncio import get_event_loop
from autoname import main as name

async def main():
  await app.start()
  await bot.start()
  try :
    await app.join_chat("SOURCE_NEON")
    await app.join_chat("FFLOOD1500")
    await app.join_chat("RB900")
    await app.join_chat("RR_BU")
  except :
    pass
  await name()
  await idle()
  


loop = get_event_loop()
loop.run_until_complete(main())