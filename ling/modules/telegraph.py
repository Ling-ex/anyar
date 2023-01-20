import os
from telegraph import upload_file

from pyrogram import filters, Client
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from .help import add_command_help

@Client.on_message(filters.command(["tm", "tgm", "telegraph"], cmd) & filters.me) 
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("harap balas ke media yang valid.")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply_text("media tidak valid!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name="root/nana/"
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await client.send_message(message.chat.id, document)
    else:
        await message.reply_text(
            f"**Document passed to: [Telegra.ph](https://telegra.ph{response[0]})**",
        )
    finally:
        os.remove(download_location)


add_command_help(
    "telegraph",
    [
        ["tm", "Reply foto/video untuk menjadikan link telegraph."],
    ],
)
