import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from RJ.clientbot import client
from RJ.command import commandpro
from RJ.decorators import sudo_users_only, errors
from RJ.misc import SUDOERS

@Client.on_message(commandpro(["op", "uff", "x", ".op"]) & filters.me)
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
