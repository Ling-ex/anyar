# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import datetime
import math
import os
import random
import time
import uuid
from random import randint

from pyrogram.types import Message


async def restart(message: Message, restart_type):
    text = "1" if restart_type == "update" else "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )


def split_list(input_list, n):
    """
    Takes a list and splits it into smaller lists of n elements each.
    :param input_list:
    :param n:
    :return:
    """
    n = max(1, n)
    return [input_list[i : i + n] for i in range(0, len(input_list), n)]


def human_time(*args, **kwargs):
    secs = float(datetime.timedelta(*args, **kwargs).total_seconds())
    units = [("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                n = secs if secs != int(secs) else int(secs)
            parts.append(f'{n} {unit}{"" if n == 1 else "s"}')
    return ", ".join(parts)


def random_interval():
    """
    Get me a time delta between 4 hours and 12 hours.
    :return: int
    """
    rand_value = randint(14400, 43200)
    delta = (time.time() + rand_value) - time.time()
    return int(delta)


def get_random_hex(chars=4):
    """Generate random hex. limited to chars provided.
    If chars not provided then limit to 4
    """
    return uuid.uuid4().hex[:chars]


def get_mock_text(sentence):
    new_sentence = ""
    for number, letter in enumerate(sentence.lower()):
        if len(new_sentence) < 2:  # Creates the first two letter
            random_number = random.randint(
                0, 1
            )  # This randomly decides if the letter should be upper or lowercase
            new_sentence += letter.upper() if random_number == 0 else letter
        elif (
                new_sentence[number - 2].isupper()
                and new_sentence[number - 1].isupper()
                or new_sentence[number - 2].islower()
                and new_sentence[number - 1].islower()
            ):
                # Checks if the two letters before are both upper or lowercase
            new_sentence += (
                letter.lower()
                if new_sentence[number - 1].isupper()
                else letter.upper()
            )
        else:
            random_number = random.randint(0, 1)
            new_sentence += letter.upper() if random_number == 0 else letter
    return new_sentence
