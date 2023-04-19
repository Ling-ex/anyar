# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os
from pyrogram import filters, Client
from pyrogram.types import Message
from py_trans import Async_PyTranslator
from config import CMD_HANDLER as cmds

from .help import add_command_help


@Client.on_message(filters.command(["tr", "translate"], cmds) & filters.me)
async def pytrans_tr(_, message: Message):
  tr_msg = await message.edit("`Processing...`")
  r_msg = message.reply_to_message
  args = get_arg(message)
  if r_msg:
    if r_msg.text:
      to_tr = r_msg.text
    else:
      return await tr_msg.edit("`Reply to a message that contains text!`")
    if not args:
      return await tr_msg.edit("`Please define a destination language!`!`")
    sp_args = args.split(" ")
    tr_engine = sp_args[1] if len(sp_args) == 2 else "google"
    dest_lang = sp_args[0]
  elif args:
    # Splitting provided arguments in to a list
    a_conts = args.split(None, 2)
    # Checks if translation engine is defined by the user
    if len(a_conts) == 3:
      tr_engine = a_conts[1]
      to_tr = a_conts[2]
    else:
      to_tr = a_conts[1]
      tr_engine = "google"
    dest_lang = a_conts[0]
  # Translate the text
  py_trans = Async_PyTranslator(provider=tr_engine)
  translation = await py_trans.translate(to_tr, dest_lang)
  # Parse the translation message
  if translation["status"] == "success":
    tred_txt = f"""
**Translation Engine**: `{translation["engine"]}`
**Translated to:** `{translation["dest_lang"]}`
**Translation:**
`{translation["translation"]}`
"""
    if len(tred_txt) > 4096:
      await tr_msg.edit("`Wah!! Translated Text So Long Tho!, Give me a minute, I'm sending it as a file!`")
      with open("translated.txt", "w+") as tr_txt_file:
        tr_txt_file.write(tred_txt)
      await tr_msg.reply_document("ptranslated_NEXAUB.txt")
      os.remove("ptranslated.txt")
      await tr_msg.delete()
    else:
      await tr_msg.edit(tred_txt)

add_command_help(
    "translate",
    [
        [
            "tr <kode bahasa> <text/reply>",
            "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa indonesia)",
        ],
    ],
)
