from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""❍ » ʜᴇʏ  {msg.from_user.mention}  ✤,

❍ » ɪ ᴀᴍ{me2},

❍ » A sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.

❍ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

❍ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᯓ𓆰𝅃꯭᳚ ⃪♔͢༎𝗥𝗜𝗦𝗛𝗨 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,♡](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="❍ 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐒ᴛʀɪɴɢ ❍", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❍ 𝐒ᴜᴘᴘᴏʀᴛ ❍", url="https://t.me/ur_support07"),
                    InlineKeyboardButton("❍ 𝐔ᴘᴅᴀᴛᴇ ❍", url="https://t.me/ur_rishu_143")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
