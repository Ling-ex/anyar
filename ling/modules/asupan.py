
from asyncio import *
from config import CMD_HANDLER as cmd
from random import *
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ling
from pyrogram import Client, enums, filters
from ling.helpers.basic import *
from ling.helpers.PyroHelpers import *
from ling import *
from .help import add_command_help

@ling.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id == -1001554560763:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    ling = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        ling.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

# WARNING PORNO VIDEO THIS !!!

@ling.on_message(filters.command(["bokep", "bkp"], cmd) & filters.me)
async def bokep(client: Client, message: Message):
    if message.chat.id == -1001664137877:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    await client.join_chat("LonteGabut")
    await asyncio.sleep(2)
    kontol = await edit_or_reply(message, "wait a minute send a porn video")
    await gather(
        kontol.delete(),
        client.send_video(message.chat.id,
        choice(
            [
                    bokep.video.file_id
                    async for bokep in client.search_messages(
                       "LonteGabut", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ling.on_message(filters.command(["ayang", "ayg"], cmd) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@ling.on_message(filters.command(["ppcp", "cpp"], cmd) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()


@ling.on_message(filters.command(["ppanime", "anim"], cmd) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()


add_command_help(
    "fundb",
    [
        [
            "asupan",
            "Asupan video TikTok",
        ],
        [f"ayang & {cmd}ayg", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"ppcp & {cmd}cpp", "Mencari Foto PP Couple Random."],
        [f"bokep & {cmd}bkp", "to send random porno videos."],
        [f"ppanime & {cmd}anim", "Mencari Foto PP Couple Anime."],
    ],
)
