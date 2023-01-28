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
from Py import join
from ling.helpers.basic import edit_or_reply
from ling.helpers.PyroHelpers import ReplyCheck
from ling.helpers.SQL.globals import gvarstatus
from ling.helpers.tools import convert_to_image
from ling.modules.bot.inline import get_readable_time
from config import CMD_HANDLER as cmd
from .updater import restart
from config import *
from ling import CMD_HELP, StartTime, app


modules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or "https://telegra.ph/file/0a4818429a8a70bb1e8da.jpg"
)
emoji = gvarstatus("ALIVE_EMOJI") or "🤖"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "Hey bro, I am hyper."


@Client.on_message(filters.command(["gue", cmd], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "🤖")
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"──「 **[ʜʏᴘᴇʀ Uꜱᴇʀʙᴏᴛ](https://github.com/Ling-ex/Ling-Ubot)** 」──\n\n"
        f"╼┅━━━━━━━━╍━━━━━━━━┅╾ \n"
        f"{emoji} <b>ʙᴏᴛ ᴠᴇʀsɪᴏɴ :</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :</b> <code>{python_version()}</code> \n"
        f"{emoji} <b>ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :</b> <code>{versipyro}</code> \n"
        f"╼┅━━━━━━━━╍━━━━━━━━┅╾ \n"
        f"➠ Mʏ Mᴀꜱᴛᴇʀ : [•Cʟɪᴄᴋ•](tg://user?id={client.me.id})\n\n"
        f"    **[Sᴜᴘᴘᴏʀᴛ](https://t.me/{GROUP})** | **[Cʜᴀɴɴᴇʟ](https://t.me/{CHANNEL})** | **[Oᴡɴᴇʀ](t.me/excute7)**"
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
        
        
@Client.on_message(filters.command(["alive"], cmd) & filters.me)
async def module_help(client: Client, message: Message):
    await join(client)
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="Alive")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}"
@Client.on_message(filters.command("setalivelogo", [.]) & filters.me)
async def setalivelogo(client: Client, message: Message):
    try:
        import ling.helpers.SQL.globals as sql
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
        import ling.helpers.SQL.globals as sql
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
        import ling.helpers.SQL.globals as sql
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
