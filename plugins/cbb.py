
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 Devloper:</b> <a href='https://t.me/ifeelscam'>SHAIKH ALI</a> \n<b> 🤖 Creator :</b> <a href='t.me/infoxe'> 𝙃𝙖𝙢𝙯𝙖 </a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton(" Source code ", url="https://t.me/+NeqCUg-QDxo2Nzll"),
                  InlineKeyboardButton("Devloper" , url= "tg://user?id=6076683960")],
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





