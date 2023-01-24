from pyrogram.types import InlineKeyboardButton, WebAppInfo
from config import CMD_HANDLER as cmd

class Data:

    text_help_menu = (
        f"──「 ** Help for HyperRobot** 」──"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
