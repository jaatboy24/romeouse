import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from Zaid import SUDO_USER
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION1

client = Client(STRING_SESSION1, API_ID, API_HASH, plugins=dict(root="Zaid.modules"))

@Client.on_message(
    filters.command(["uff", "op"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await client.download_media(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)


add_command_help(
    "Uff",
    [
        ["uff", "<username and count>`."],
        ["op", "<username and count>`."],
    ],
)
