from pyrogram.types import InlineKeyboardButton, WebAppInfo
from config import CMD_HANDLER as cmd

class Data:

    text_help_menu = (
        f"**Command List & Help**\n**Prefix: . - ? ^"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
