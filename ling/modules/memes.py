# ~ported from telethon friday

import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from ling.helpers.basic import get_text
from config import CMD_HANDLER as cmd

from .help import *


@Client.on_message(filters.command("trump", cmd) & filters.me)
async def trump_tweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.edit("**Trump :** ``What Should I Tweet For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Trump Has Tweeted** {text}"
    await message.edit("**Trump:** Wait I Am Tweeting Your Text")
    await client.send_photo(message.chat.id, tweet, caption=starkxd)
    await message.delete()


@Client.on_message(filters.command("ctweet", cmd) & filters.me)
async def custom_tweet(client: Client, message: Message):
    text = get_text(message)
    input_str = get_text(message)
    if text:
        if ":" in text:
            stark = input_str.split(":", 1)
        else:
            await message.edit("**Usage Syntax :** `username:tweet-text`")
    if len(stark) != 2:
        await message.edit("**Usage Syntax :** `username:tweet-text`")
        return

    starky = stark[0]
    ipman = stark[1]
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={starky}&text={ipman}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**{starky} Has Tweeted** ``{ipman}``"
    await message.edit(f"**{starky}** : Wait I Am Tweeting Your Texts")
    await client.send_photo(message.chat.id, tweet, caption=starkxd)
    await message.delete()


add_command_help(
    "memes",
    [
        ["trump", "make a Quote by Trump."],
        ["ctweet", "Twitte by Ur values."],
    ],
)
