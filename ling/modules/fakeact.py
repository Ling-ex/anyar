# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from asyncio import sleep

from pyrogram import Client, enums, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from ling.helpers.PyroHelpers import ReplyCheck
from config import CMD_HANDLER as cmd

from .help import add_command_help

commands = {
    "ftyp": enums.ChatAction.TYPING,
    "fvid": enums.ChatAction.RECORD_VIDEO,
    "faud": enums.ChatAction.RECORD_AUDIO,
    "frou": enums.ChatAction.RECORD_VIDEO_NOTE,
    "fpho": enums.ChatAction.UPLOAD_PHOTO,
    "fstick": enums.ChatAction.CHOOSE_STICKER,
    "fdoc": enums.ChatAction.UPLOAD_DOCUMENT,
    "floc": enums.ChatAction.FIND_LOCATION,
    "fgame": enums.ChatAction.PLAYING,
    "fcon": enums.ChatAction.CHOOSE_CONTACT,
    "fstop": enums.ChatAction.CANCEL,
    "fscreen": "screenshot",
}


@Client.on_message(filters.command(list(commands), cmd) & filters.me)
async def fakeactions_handler(client: Client, message: Message):
    cmd = message.command[0]
    try:
        sec = int(message.command[1])
        sec = min(sec, 60)
    except:
        sec = None
    await message.delete()
    action = commands[cmd]
    try:
        if action == "screenshot":
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.1)
        elif sec and action != enums.ChatAction.CANCEL:
            await client.send_chat_action(chat_id=message.chat.id, action=action)
            await sleep(sec)
        else:
            return await client.send_chat_action(
                chat_id=message.chat.id, action=action
            )
    except Exception as e:
        return await client.send_message(
            message.chat.id,
            f"**ERROR:** `{e}`",
            reply_to_message_id=ReplyCheck(message),
        )


add_command_help(
    "fakeaction",
    [
        ["ftyp [detik]", "Menampilkan Pengetikan Palsu dalam obrolan."],
        ["fgame [detik]", "Menampilkan sedang bermain game Palsu dalam obrolan."],
        [
            "faud [detik]",
            "Menampilkan tindakan merekam suara palsu dalam obrolan.",
        ],
        [
            "fvid [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            "frou [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            "fpho [detik]",
            "Menampilkan tindakan mengirim foto palsu dalam obrolan.",
        ],
        [
            "fstick [detik]",
            "Menampilkan tindakan memilih Sticker palsu dalam obrolan.",
        ],
        [
            "fcon [detik]",
            "Menampilkan tindakan Share Contact palsu dalam obrolan.",
        ],
        [
            "floc [detik]",
            "Menampilkan tindakan Share Lokasi palsu dalam obrolan.",
        ],
        [
            "fdoc [detik]",
            "Menampilkan tindakan tengirim Document/File palsu dalam obrolan.",
        ],
        [
            "fscreen [jumlah]",
            "Menampilkan tindakan screenshot palsu. (Gunakan di Obrolan Pribadi)",
        ],
        ["fstop", "Memberhentikan tindakan palsu dalam obrolan."],
    ],
)
