# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>UPDATE CHANNEL:</b> <a href='https://t.me/Publicfille'>CLICK HERE</a> \n<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>  \n<b>🧑‍💻 Developer :</b> <a href='t.me/ifeelscam'>HAMZA</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [InlineKeyboardButton("Source Code", url = "https://t.me/+NeqCUg-QDxo2Nzll"),
                  InlineKeyboardButton("Update Channel", url = "https://t.me/publicfille")],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
