# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *
from ling.helpers.basic import edit_or_reply
from ling.utils import extract_user
from config import CMD_HANDLER as cmd

from .help import add_command_help


@Client.on_message(filters.command(["sm", "sg", "sangmata"], cmd) & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit("<code>Processing...</code>")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
         return await lol.edit("<code>Please specify a valid user!</code>")
    sg = -1001936325181
    try:
         await client.join_chat("https://t.me/+ZlDl0da5ag9jYWRl")
         await asyncio.sleep(0.5)
         await client.send_message(sg, f"@Sangmata_beta_bot Allhistory {user.id}")
    except:
         return
    await asyncio.sleep(1)
    async for stalk in client.search_messages(sg, limit=1):
        if not stalk:
            await message.edit("<code>Orang Ini Belum Pernah Mengganti Namanya</code>")
            return
        elif stalk:
            await message.edit(stalk.text)
            await client.leave_chat(sg)

add_command_help(
    "sangmata",
    [
        [
            f"{cmd}sm <reply/userid/username>",
            "Untuk Mendapatkan Riwayat Nama Pengguna selama di telegram.",
        ],
    ],
)
