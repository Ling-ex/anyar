# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
# null
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram.helpers.PyroHelpers import ReplyCheck
from geezlibs.ram.helpers.SQL.globals import gvarstatus
from geezlibs.ram.helpers.tools import convert_to_image
from geezlibs.ram.utils import get_readable_time
from geezlibs.ram.utils.misc import restart
from config import BOT_VER, CHANNEL
from config import CMD_HANDLER as cmd
from config import GROUP
from rams import CMD_HELP, StartTime


from .help import add_command_help

modules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or "https://telegra.ph/file/eda4816a97d4e74445fc0.jpg"
)
emoji = gvarstatus("ALIVE_EMOJI") or "🤖"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "Hey bro, I am rams."


@Client.on_message(filters.command(["alive", "gue"], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "🤖")
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"**꧁༺[RamPyro-Bot](https://github.com/ramadhani892/RamPyro-Bot)༻꧂**\n\n"
        f"━───────╯•╰───────━\n"
        f"{emoji} <b>ʙᴏᴛ ᴠᴇʀsɪᴏɴ :</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :</b> <code>{python_version()}</code> \n"
        f"{emoji} <b>ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :</b> <code>{versipyro}</code> \n"
        f"━───────╮•╭───────━\n"
        f"➠ 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 : [❝𝐂𝐥𝐢𝐜𝐤❞ ](tg://user?id={client.me.id}) \n\n"
        f"    **[𝚂𝚞𝚙𝚙𝚘𝚛𝚝](https://t.me/{GROUP})** | **[𝙲𝚑𝚊𝚗𝚗𝚎𝚕](https://t.me/{CHANNEL})** | **[𝙾𝚠𝚗𝚎𝚛](t.me/thisrama)**"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(man, disable_web_page_preview=True)


@Client.on_message(filters.command("setalivelogo", cmd) & filters.me)
async def setalivelogo(client: Client, message: Message):
    try:
        import rams.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    Man = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Man.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await Man.edit(
        f"**Berhasil Mengcustom ALIVE LOGO Menjadi {link}**",
        disable_web_page_preview=True,
    )
    restart()


@Client.on_message(filters.command("setalivetext", cmd) & filters.me)
async def setalivetext(client: Client, message: Message):
    try:
        import rams.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    Man = await edit_or_reply(message, "`Processing...`")
    if not text:
        return await edit_or_reply(
            message, "**Berikan Sebuah Text atau Reply ke text**"
        )
    sql.addgvar("ALIVE_TEKS_CUSTOM", text)
    await Man.edit(f"**Berhasil Mengcustom ALIVE TEXT Menjadi** `{text}`")
    restart()


@Client.on_message(filters.command("setemoji", cmd) & filters.me)
async def setemoji(client: Client, message: Message):
    try:
        import rams.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    emoji = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    Man = await edit_or_reply(message, "`Processing...`")
    if not emoji:
        return await edit_or_reply(message, "**Berikan Sebuah Emoji**")
    sql.addgvar("ALIVE_EMOJI", emoji)
    await Man.edit(f"**Berhasil Mengcustom EMOJI ALIVE Menjadi** {emoji}")
    restart()


add_command_help(
    "alive",
    [
        [
            "alive",
            "Untuk memeriksa userbot anda berfungsi atau tidak",
        ],
        [
            "setalivelogo <link telegraph atau reply ke foto/video/gif>",
            "Untuk mengcustom alive logo userbot anda",
        ],
        [
            "setalivetext <text>",
            "Untuk mengcustom alive text userbot anda",
        ],
        [
            "setemoji <emoji>",
            "Untuk mengcustom emoji alive userbot anda",
        ],
    ],
)
