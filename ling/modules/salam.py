# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from hyperlibs.ling.helpers.basic import edit_or_reply
from hyperlibs.ling.helpers.PyroHelpers import ReplyCheck
from config import CMD_HANDLER as cmd
from config import IG_ALIVE, CH_SFS
from .help import add_command_help


@Client.on_message(filters.command("p", cmd) & filters.me)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Anak Goblok!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pe", cmd) & filters.me)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("l", cmd) & filters.me)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Kaum Dajal",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("el", cmd) & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("oi", cmd) & filters.me)
async def salken(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Haii Salken Saya {client.me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("Kalian Anjing,Anak Haram Titisan Asmodeus, Bocah tengik, Penyembah tongkat Kera Sakti")


@Client.on_message(filters.command("ass", cmd) & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


@Client.on_message(filters.command("j", cmd) & filters.me)
async def jakasem(client: Client, message: Message):
    xx = await edit_or_reply(message, "**Woi Kontol....**")
    await asyncio.sleep(3)
    await xx.edit("**Muka lo jelek Bgt Kaya kontol!!!🔥**")


@Client.on_message(filters.command("k", cmd) & filters.me)
async def ngegas(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Hallo KIMAAKK SAYA {client.me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("**LU SEMUA NGENTOT 😂**")


@Client.on_message(filters.command("mutu", cmd) & filters.me)
async def igehh(client: Client, message: Message):
    xx = await edit_or_reply(message, "**Mutualan IG Yuk!!**")
    await asyncio.sleep(2)
    await xx.edit(f"nih IG ku = [TEKAN](https://instagram.com/{IG_ALIVE})")


@Client.on_message(filters.command("sfs", cmd) & filters.me)
async def channel(client: Client, message: Message):
    xx = await edit_or_reply(message, "**Yok SFS!!**")
    await asyncio.sleep(2)
    await xx.edit(f"nih CH ku = [TEKAN](https://t.me/{CH_SFS})")


@Client.on_message(filters.command("keluar", cmd) & filters.me)
async def keluar(client: Client, message: Message):
    xx = await edit_or_reply(message, "`Processing...`")
    await asyncio.sleep(1)
    await xx.edit(f"{client.me.first_name} has left this group, bye!!")


add_command_help(
    "salam",
    [
        ["p", "Assalamualaikum."],
        ["pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        ["l", "Wa'alaikumsalam."],
        ["ass", "Assalamualaikum Bahas arab."],
        ["oi", "Salam Kenal dan salam."],
        ["l", "Wa'alaikumsalam."],
        ["el", "Wa'alaikumsalam Warahmatullahi Wabarakatuh."],
    ],
)

add_command_help(
    "sfs",
    [
        ["sfs", "Subs for Subs Channel."],
        ["mutu", "Mutualan Ig cuyyyy,"],
    ],
)
