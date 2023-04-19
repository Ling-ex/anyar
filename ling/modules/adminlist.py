# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ling.helpers.basic import edit_or_reply
from ling.helpers.parser import mention_html, mention_markdown
from ling.modules.help import *


@Client.on_message(filters.me & filters.command(["admins", "adminlist"], cmd))
async def adminlist(client: Client, message: Message):
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    grup = await client.get_chat(chat)
    replyid = message.reply_to_message.id if message.reply_to_message else None
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            nama = f"{a.user.first_name} {a.user.last_name}"
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, nama))
            else:
                admin.append(mention_markdown(a.user.id, nama))
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(a.user.id, nama))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = f"**Admins in {grup.title}**\n" + "╒═══「 Creator 」\n"
    for x in creator:
        teks += f"│ • {x}\n"
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"╞══「 {len(admin)} Human Administrator 」\n"
    for x in admin:
        teks += f"│ • {x}\n"
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"╞══「 {len(badmin)} Bot Administrator 」\n"
    for x in badmin:
        teks += f"│ • {x}\n"
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"╘══「 Total {totaladmins} Admins 」"
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


@Client.on_message(filters.command(["kickdel", "zombies"], cmd) & filters.me)
async def kickdel_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "<b>Kicking deleted accounts...</b>")
    # noinspection PyTypeChecker
    values = [
        await message.chat.ban_member(user.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    await Man.edit(f"<b>Successfully kicked {len(values)} deleted account(s)</b>")


@Client.on_message(
    filters.me & filters.command(["reportadmin", "reportadmins", "report"], cmd)
)
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    admin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        if (
            a.status
            in [
                enums.ChatMemberStatus.ADMINISTRATOR,
                enums.ChatMemberStatus.OWNER,
            ]
            and not a.user.is_bot
        ):
            admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        teks = (
            f"{text}"
            if text
            else f"{mention_html(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)} reported to admins."
        )
    else:
        teks = f"{html.escape(text)}" if text else f"Calling admins in {grup.title}."
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            teks,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, teks, parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(filters.me & filters.command(["everyone", "tagall"], cmd))
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "Hi all 🙃"
    kek = client.get_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            text,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, text, parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(filters.me & filters.command(["botlist", "bots"], cmd))
async def get_list_bots(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    grup = await client.get_chat(chat)
    replyid = message.reply_to_message.id if message.reply_to_message else None
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            nama = f"{a.user.first_name} {a.user.last_name}"
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = f"**All bots in group {grup.title}**\n" + "╒═══「 Bots 」\n"
    for x in bots:
        teks += f"│ • {x}\n"
    teks += f"╘══「 Total {len(bots)} Bots 」"
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


add_command_help(
    "tag",
    [
        [f"{cmd}admins", "Get chats Admins list."],
        [f"{cmd}kickdel", "To Kick deleted Accounts."],
        [
            f"{cmd}everyone `or` {cmd}tagall",
            "to mention Everyone ",
        ],
        [
            f"{cmd}botlist",
            "To get Chats Bots list",
        ],
    ],
)
