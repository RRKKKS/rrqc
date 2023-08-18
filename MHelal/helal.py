#'‹ ٰ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ🇪🇬 › .'#
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import redis, re
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import redis, re 
API_ID = int("23188747")
API_HASH = "33f7e93d85538b811cdb354b83697009"
Bots = []
off =None
DEVS = ["R_R_B0"] #يوزرات المطورين المصنع
BOTY= "6013874411:AAF95252Q7i6sqOTpDEkBKAca949CxIvIJU"
app = Client("remymbot",
  api_id=9398500, api_hash="ad2977d673006bed6e5007d953301e13",
  bot_token=BOTY, 
)
bot_id = ("5345637082")[0]

# create a Redis client
r = redis.Redis(
    host="127.0.0.1",
    port=6379,)


@Client.on_message(filters.private)
async def me(client, message):
   if off:#'‹ َٰٰ𝙎ُِ𝙊ِّ𝙐ٓ𝙍ٍّ𝘾ٍ𝙀 ٌٍ𝙓ٍ𝘽🇪🇬 › .'#
    if not message.from_user.username in DEVS:
     return await message.reply_text("الصانع معطل من قبل مطور الصانع \n للتواصل مع المطور : @R_R_B0")
   message.continue_propagation()

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
   if message.from_user.username in DEVS:
     kep = ReplyKeyboardMarkup([["✭ صنع بوت", "✭ حذف بوت"], ["✭ البوتات المصنوعه"], ["✭ تعطيل المجاني", "✭ تفعيل المجاني"], ["✭ السورس"],["اخفاء الكيبورد"],["الاحصائيات"],["تفعيل التواصل","تعطيل التواصل"],["• اوامر الاذاعة للخاص •"],["اذاعة بالتثبيت","اذاعة","اذاعة بالتوجيه"],["• اوامر الاذاعة بالجروبات •"],["اذاعة بالمجموعات","اذاعة بالتثبيت بالمجموعات"],["تفعيل الاشتراك", "تعطيل الاشتراك"],["ضع قناة الاشتراك","حذف قناة الاشتراك"],["قناة الاشتراك"],["رفع ادمن","تنزيل ادمن"],["قائمه الأدمنيه"],["المستخدمين","الأدمنية","الجروبات"],["نقل ملكية البوت"],["الغاء"]], resize_keyboard=True)
     return await message.reply_text("اهلا بيك ف مصنع بوتات xb ميوزك", reply_markup=kep)
   kep = ReplyKeyboardMarkup([["✭ صنع بوت", "✭ حذف بوت"], ["✭ السورس"]], resize_keyboard=True)
   await message.reply_text("اهلا بيك ف مصنع تيلثون فينوم \n للتواصل مع المطور : @R_R_B0", reply_markup=kep)

@Client.on_message(filters.command(["✭ السورس"], ""))
async def alivehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝙶𝚁𝙾𝚄𝙿️", url=f"https://t.me/r_n_b1"),
                InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴️", url=f"https://t.me/source_neon"),
            ],
            [
                 InlineKeyboardButton(f"𓏺 DEV VENOM  .", url=f"https://t.me/r_r_b0")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/ff96e7a4714736bc836df.jpg",
        caption="",
        reply_markup=keyboard,
    )
@Client.on_message(filters.command(["✭ تفعيل المجاني", "✭ تعطيل المجاني"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.username in DEVS:
    return
  global off
  if message.text == "✭ تفعيل المجاني":
    off = None
    return await message.reply_text("✭ تم تفعيل الوضع المجاني بنجاح")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح ✭")
@Client.on_message(filters.command("✭ صنع بوت", "") & filters.private)
async def makedhelal(client, message):
  if not message.from_user.username in DEVS:
    for x in Bots:
        if x[1] == message.from_user.id:
          return await message.reply_text("لقد قمت بصنع بوت من قبل ✭")
  try:
    ask = await client.ask(message.chat.id, "✭ ارسل توكن البوت", timeout=300)
  except:
      return
  TOKEN = ask.text
  try:
    ask = await client.ask(message.chat.id, "✭ ارسل كود الجلسه", timeout=300)
  except:
      return
  SESSION = ask.text
  try:
    ask = await client.ask(message.chat.id, "ارسل الان ايدي جروب التخزين ✭", timeout=300)
  except:
      return
  LOG = ask.text
  try:
       ask = await client.ask(message.chat.id, "✭ ارسل ايدي المطور", timeout=300)
  except:
    return
  try:
      Dev = int(ask.text)
  except:
      return await message.reply_text("قم بارسال الايدي بشكل صحيح") #'‹ َٰٰ𝙎ُِ𝙊ِّ𝙐ٓ𝙍ٍّ𝘾ٍ𝙀 ٌٍ𝙓ٍ𝘽 › .'#
  bot = Client(f"{TOKEN}", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
  user = Client(f"{Dev}",api_id=API_ID, api_hash=API_HASH, session_string=str(SESSION))
  try:
    await bot.start()
    username = await bot.get_me()
    username = username.username
    await bot.stop()
    await user.start()
    await user.stop()
  except:
    return await message.reply_text("✭ تاكد من التوكن أو الجلسة")
  id = username
  for x in Bots: 
      if x[0] == id:
          return await message.reply_text("لقد قمت بصنع هذا البوت من قبل ✭")
  os.system(f"cp -a source users/{id}")
  env = open(f"users/{id}/config.py", "w+", encoding="utf-8")
  x = f'from pyrogram import Client,filters,enums\nimport redis\nr = redis.Redis(\n    host="127.0.0.1",\n    port=6379,\n    charset="utf-8",\n    decode_responses=True\n    )\nsudo_id = {Dev}\nbot_user = "{id}"\napi_id = 10823881\napi_hash = "339886e2109eb67203ce12022b32e035"\nsession = "{SESSION}"\ntoken = "{TOKEN}"\nsudo_command = [5345637082, 1001132193]\npm = "{LOG}"\nmention = "{LOG}"\nplugins = dict(root="plugins")\napp = Client("user:{id}",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)\nbot = Client("{id}",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))\n'
  env.write(x)
  env.close()
  os.system(f"cd users/{id} && screen -d -m -S {id} python3.8 -m user.py")
  oo = [id, Dev]
  Bots.append(oo)
  await message.reply_text("تم صنع  بوتك بنجاح ✭")

@Client.on_message(filters.command("✭ حذف بوت", "") & filters.private)
async def deletbothelal(client, message):
   if not message.from_user.username in DEVS:
     for x in Bots:
         bot = x[0]
         if x[1] == message.from_user.id:       
           os.system(f"rm -fr users/{bot}")
           os.system(f"screen -XS {bot} quit")
           Bots.remove(x)
           return await message.reply_text("تم حذف بوتك من الصانع ✭")
     return await message.reply_text("✭ لم تقم بصنع بوتات")
   try:
      bot = await client.ask(message.chat.id, "✭ هات يوزر البوت", timeout=200)
   except:
      return
   bot = bot.text.replace("@", "")
   for x in Bots:
       if x[0] == bot:
          Bots.remove(x)
   os.system(f"rm -fr users/{bot}")
   os.system(f"screen -XS {bot} quit")
   await message.reply_text("✭ تم حذف البوت بنجاح")


@Client.on_message(filters.command("✭ البوتات المصنوعه", ""))
async def bothelal(client, message):
  if not message.from_user.username in DEVS:
   return
  o = 0
  text = "قايمه البوتات\n"
  for x in Bots:#'‹ َٰٰ𝙎ُِ𝙊ِّ𝙐ٓ𝙍ٍّ𝘾ٍ𝙀 ٌٍ𝙓ٍ𝘽🇪🇬 › .'#
      o += 1
      text += f"{o}- @{x[0]}\n"
  if o == 0:
    return await message.reply_text("لا يوجد بوتات مصنوعه")
  await message.reply_text(text)

@app.on_message(filters.private, group=9)
async def twasol__(app,m):
   if not check(m.from_user.id):
       await m.forward(int(r.get(f"bot_owner{bot_id}")))
   
   if m.from_user.id == 5345637082:
      if m.reply_to_message:
        if m.reply_to_message.forward_from:
          await m.reply(f"• تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
          try:
            await m.copy(m.reply_to_message.forward_from.id)
          except:
            pass
      