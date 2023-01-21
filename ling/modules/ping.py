# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
from datetime import datetime
import asyncio
import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from ling.helpers.basic import edit_or_reply
from ling.helpers.constants import WWW
from ling.helpers.PyroHelpers import SpeedConvert
from ling.utils.tools import get_readable_time
from ling.helpers.adminHelpers import DEVS
from ling.helpers.PyroHelpers import ReplyCheck
from config import BOT_VER, CMD_HANDLER as cmd
from config import GROUP, BRANCH as branch
from ling import CMD_HELP, StartTime
from .help import add_command_help

modules = CMD_HELP



@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("ceping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("rping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(message, "**Mengecek Sinyal...**")
    await ram.edit("**▁**")
    await ram.edit("**▁ ▂**")
    await ram.edit("**▁ ▂ ▄**")
    await ram.edit("**▁ ▂ ▄ ▅**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇ █**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆**")
    await ram.edit("**▁ ▂ ▄ ▅ **")
    await ram.edit("**▁ ▂ ▄**")
    await ram.edit("**▁ ▂**")
    await ram.edit("**▁**")
    await ram.edit("**▁ ▂**")
    await ram.edit("**▁ ▂ ▄**")
    await ram.edit("**▁ ▂ ▄ ▅**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇**")
    await ram.edit("**▁ ▂ ▄ ▅ ▆ ▇ █**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await ram.edit(
        f"**ʜʏᴘᴇʀ-ᴜʙᴏᴛ⌛**\n"
        f"** ➠  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ➠  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ➠  Oᴡɴᴇʀ   :** {client.me.mention}" % (duration)
    )


@Client.on_message(
    filters.command("dping", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("ping", cmd) & filters.me)
async def kping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"**Hʏᴘᴇʀ-Uʙᴏᴛ**\n"
        f"**Pɪɴɢ:** "
        f"`%sms` \n"
        f"**Uᴘᴛɪᴍᴇ:** "
        f"`{uptime}` \n"
        f"**Oᴡɴᴇʀ:** {client.me.mention}" % (duration)
    )


@Client.on_message(filters.command("ling", cmd) & filters.me)
async def ramping(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        text="\n"
        "ㅤㅤStatus : Hʏᴘᴇʀ-Uʙᴏᴛ Menyala!\n"
        f"ㅤㅤㅤㅤping bot:"
        f"`%sms` \n"
        f"ㅤㅤㅤㅤmodules:</b> <code>{len(modules)} Modules</code> \n"
        f"ㅤㅤㅤㅤbot version: {BOT_VER} \n"
        f"ㅤㅤㅤㅤbot uptime:"
        f"`{uptime}` \n"
        f"ㅤㅤㅤㅤbranch: {branch} \n\n"
        f"ㅤㅤㅤㅤOwner : {client.me.mention}" % (duration),
    )
        
add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["rping", "Untuk Menunjukkan Ping Bot Anda ( Beda animasi doang )."],
    ],
)
