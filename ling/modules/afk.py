# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time

from pyrogram import Client, filters
from pyrogram.types import Message
from ling.helpers.msg_types import Types, get_message_type
from ling.helpers.parser import escape_markdown, mention_markdown
from ling.helpers.SQL.afk_db import get_afk, set_afk
from config import CMD_HANDLER as cmd
from ling import BOTLOG_CHATID
from ling.modules.help import add_command_help

# Set priority to 11 and 12
MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 3  # seconds


@Client.on_message(filters.me & filters.command("afk", cmd))
async def afk(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        set_afk(True, message.text.split(None, 1)[1])
        await message.edit(
            f"🤖 {mention_markdown(message.from_user.id, message.from_user.first_name)} <b>Telah AFK!</b>\n└ <b>Karena:</b> <code>{message.text.split(None, 1)[1]}</code>"
        )
    else:
        set_afk(True, "")
        await message.edit(
            f"{mention_markdown(message.from_user.id, message.from_user.first_name)} <b>Telah AFK</b>"
        )
    await message.stop_propagation()


@Client.on_message(
    (filters.mentioned | filters.private) & filters.incoming & ~filters.bot, group=11
)
async def afk_mentioned(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        if "-" in str(message.chat.id):
            cid = str(message.chat.id)[4:]
        else:
            cid = str(message.chat.id)

        if cid in list(AFK_RESTIRECT) and int(AFK_RESTIRECT[cid]) >= int(
            time.time()
        ):
            return
        AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
        if get["reason"]:
            await message.reply(
                f'🤖 {client.me.mention} <b>Sedang AFK!</b>\n└ <b>Karena:</b> <code>{get["reason"]}</code>'
            )
        else:
            await message.reply(
                f"<b>Maaf</b> {client.me.first_name} <b>Sedang AFK!</b>"
            )

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            text = message.text if message.text else message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {
                "user": message.from_user.first_name,
                "user_id": message.from_user.id,
                "chat": message.chat.title,
                "chat_id": cid,
                "text": text,
                "message_id": message.id,
            }
        )
        try:
            await client.send_message(
                BOTLOG_CHATID,
                f"<b>#MENTION\n • Dari :</b> {message.from_user.mention}\n • <b>Grup :</b> <code>{message.chat.title}</code>\n • <b>Pesan :</b> <code>{text[:3500]}</code>",
            )
        except BaseException:
            pass


@Client.on_message(filters.me & filters.group, group=12)
async def no_longer_afk(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        set_afk(False, "")
        try:
            await client.send_message(BOTLOG_CHATID, "Anda sudah tidak lagi AFK!")
        except BaseException:
            pass
        text = f"<b>Total {len(MENTIONED)} Mention Saat Sedang AFK<b>\n"
        for x in MENTIONED:
            msg_text = x["text"]
            if len(msg_text) >= 11:
                msg_text = f'{x["text"]}...'
            text += f'- [{escape_markdown(x["user"])}](https://t.me/c/{x["chat_id"]}/{x["message_id"]}) ({x["chat"]}): {msg_text}\n'
        try:
            await client.send_message(BOTLOG_CHATID, text)
        except BaseException:
            pass
        MENTIONED = []


add_command_help(
    "afk",
    [
        [
            "afk <alasan>",
            "Memberi tahu orang yang menandai atau membalas salah satu pesan atau dm anda kalau anda sedang afk",
        ],
    ],
)
