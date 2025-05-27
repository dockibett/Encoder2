from pyrogram import filters
from pyrogram import idle
from bot import bot, data, Config, LOGS, queue, list_handler, words
import asyncio
from bot.database import adduser, napana
import traceback
import time
from datetime import datetime
from bot.plugins.compress import mediainfo, renew, sysinfo
from bot.plugins.utils import add_task1, on_task_complete
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from .plugins.devtools import exec_message_f, eval_message_f
from .plugins.extras import changeffmpeg , get_ffmpeg, upload_dir, download_dir, get_type, changemode, sample, vshots


START_TIME = datetime.now()

@bot.on_message(filters.incoming & filters.command(["start"]))
async def help_message(bot, message):
  await adduser(message)
  
  first_name = message.from_user.first_name
  uptime_str = str(datetime.now() - START_TIME).split('.')[0]
  txt = f"🤖 Hi **{first_name}**, Welcome to **CHOCKTI Encoder** bot!\n\nThis is a very powerful Telegram bot. You can encode video with the desired FFmpeg settings. Keeps coding even after reboot due to database.\n\n◉ **Bot Uptime:** {uptime_str} \n\n◉𝙹𝙾𝙸𝙽 CHANNEL 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴🔐"

  await bot.send_message(
        chat_id=message.chat.id,
        text=txt,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('**Jᴏɪɴ ɴᴏᴡ 🔓**', url='https://t.me/ChocktorBet')

                ],
                [
                   InlineKeyboardButton('**Jᴏɪɴ ɴᴏᴡ **', url='https://t.me/Doctor_original')
                   
                ]
            ]
        ),
        reply_to_message_id=message.id,
    )


@bot.on_message(filters.incoming & (filters.video | filters.document))
async def help_message(bot, message):
  if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
   return await message.reply_text("⛔️ **Sorry, You Are Not An Authorized User!** Contact: [Docki](https://t.me/Doctor_original) ⛔️", quote=True)
  query = await message.reply_text("⏰ **Added To QUEUE ...                                            Pleas be patient,Encodling will start soon**", quote=True)
  queue.insert_one({'message' : str(message)})
  await napana()
  if len(data) == 1:
   await query.delete()
   await add_task1(data[0])


@bot.on_message(filters.incoming & filters.command(["simp"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await sample(bot, message)


@bot.on_message(filters.incoming & filters.command(["vshot"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await vshots(bot, message)


@bot.on_message(filters.incoming & filters.command(["info"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await mediainfo(bot, message)


@bot.on_message(filters.incoming & filters.command(["getcode"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await get_ffmpeg(bot, message)


@bot.on_message(filters.incoming & filters.command(["setcode"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await changeffmpeg(bot, message)


@bot.on_message(filters.incoming & filters.command(["ulmode"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await get_type(bot, message)


@bot.on_message(filters.incoming & filters.command(["setul"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await changemode(bot, message)


@bot.on_message(filters.incoming & filters.command(["ul"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await upload_dir(bot, message)


@bot.on_message(filters.incoming & filters.command(["dl"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await download_dir(bot, message)


@bot.on_message(filters.incoming & filters.command(["sysinfo"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.AUTH_USERS + Config.ADMIN + Config.OWNER):
      return await message.reply_text("🚫 **You Are Not Authorized To Use This Bot. Contact: [Docki](https://t.me/Doctor_original)**", disable_web_page_preview=True, quote=True)
    await sysinfo(message)


@bot.on_message(filters.incoming & filters.command(["renew"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.ADMIN + Config.OWNER):
      return await message.reply_text("**Access Denied.** 🔒", quote=True)
    await renew(message)


@bot.on_message(filters.incoming & filters.command(["clear"]))
async def help_message(bot, message):
    if message.chat.id not in (Config.ADMIN + Config.OWNER):
      return await message.reply_text("**Access Denied.** 🔒", quote=True)
    data.clear()
    list_handler.clear()
    queue.delete_many({})
    await message.reply_text("🚮 **┌─────═━┈━═─────┐\nCleared The Queue\n└─────═━┈━═─────┘**", quote=True)


@bot.on_message(filters.incoming & filters.command(["logs"]))
async def help_message(bot, message):
    if message.chat.id not in Config.OWNER:
      return await message.reply_text("🛑 **Error 401: Not Authorized.**", quote=True)
    await message.reply_document('Logs.txt', quote=True)


@bot.on_message(filters.incoming & filters.command(["bash"]))
async def help_message(bot, message):
    if message.chat.id not in Config.OWNER:
      return await message.reply_text("🛑 **Error 401: Not Authorized.**", quote=True)
    await exec_message_f(bot, message)


@bot.on_message(filters.incoming & filters.command(["eval"]))
async def help_message(bot, message):
    if message.chat.id not in Config.OWNER:
      return await message.reply_text("🛑 **Error 401: Not Authorized.**", quote=True)
    await eval_message_f(bot, message)


@bot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = "Hi! {} Here is a list of all my commands \n \n 1 . `start⚡️` \n 2. `help📚` \n 3. `login🔑` \n 4.`follow❤️` \n 5. `ping📡` \n 6. `status📊` \n 7. `DC` this tells your telegram dc \n 8. `maintainers😎` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
async def checkup():
 try:
  await napana()
  if len(data) >= 1:
   LOGS.info("adding task")
   await add_task1(data[0])
 except Exception as e:
  LOGS.info(e)


async def startup():
    await bot.start()
    LOGS.info(f'[Started]: @{(await bot.get_me()).username}')
    x = len(Config.OWNER)
    for i in range(0, x):
      await bot.send_message(chat_id=Config.OWNER[i], text="🔄 **Bot Has Ꮢᴇsᴛᴀrᴛᴇd.** 😉")
    LOGS.info("STARTING CHECKUP")
    await checkup()
    await idle()
    await bot.stop()


bot.loop.run_until_complete(startup())
