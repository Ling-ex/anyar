import asyncio
import socket
import sys
import os
from re import sub
from time import time
import aiohttp
import requests
import asyncio
from os import getenv
import shlex
import textwrap
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

from pyrogram import enums
from datetime import datetime
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from pyrogram import Client, filters
from pyrogram.types import Message
from ling import *
from ling.helpers import *
from ling.utils import *
from config import CMD_HANDLER as cmd
from config import GIT_TOKEN, REPO_URL, BRANCH
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
from ling import *
from .help import add_command_help
HAPP = None


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]

BASE = "https://batbin.me/"

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return " ".join(split[1:]) if " ".join(split[1:]).strip() else ""


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def PasteBin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    return BASE + resp["message"]

if GIT_TOKEN:
    GIT_USERNAME = REPO_URL.split("com/")[1].split("/")[0]
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
UPSTREAM_REPO_URL = UPSTREAM_REPO if GIT_TOKEN else REPO_URL
requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "ling"])

async def is_heroku():
    return "heroku" in socket.getfqdn()

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)
        
@Client.on_message(filters.command("restart", cmd) & filters.user(DEVS) & ~filters.me)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot has restarted !**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "ling"]
        execle(sys.executable, *args, environ)


@Client.on_message(
    filters.command(["shotdown", "off"], cmd) & filters.user(DEVS) & ~filters.me)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**#SHUTDOWN** \n"
            "**Pertamax Userbot** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await message.reply("✔️ **Pertamax Userbot Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)

@Client.on_message(filters.command("hupdate", ".") & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("update", cmd) & filters.me)
async def upstream(client: Client, message: Message):
    status = await message.edit_text("`Checking for Updates, Wait a Moment...`")
    conf = get_arg(message)
    off_repo = UPSTREAM_REPO_URL
    try:
        txt = (
            "**Update Could Not Continue Due "
            + "Several ERROR Occurred**\n\n**LOGTRACE:**\n"
        )
        repo = Repo()
    except NoSuchPathError as error:
        await status.edit(f"{txt}\n**Directory** `{error}` **Can not be found.**")
        repo.__del__()
        return
    except GitCommandError as error:
        await status.edit(f"{txt}\n**Early failure!** `{error}`")
        repo.__del__()
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != BRANCH:
        await status.edit(
            f"**[UPDATER]:** `Looks like you are using your own custom branch ({ac_br}). in that case, Updater is unable to identify which branch is to be merged. please checkout to main branch`"
        )
        repo.__del__()
        return
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    if "deploy" not in conf:
        if changelog:
            changelog_str = f"**Update Available For Branch [{ac_br}]:\n\nCHANGELOG:**\n\n`{changelog}`"
            if len(changelog_str) <= 4096:
                return await status.edit(
                    f"{changelog_str}\n**Type** `.update deploy` **To Update Userbot.**",
                    disable_web_page_preview=True,
                )
            await status.edit("**Changelog too big, sent as file.**")
            with open("output.txt", "w+") as file:
                file.write(changelog_str)
            await client.send_document(
                message.chat.id,
                "output.txt",
                caption="**Type** `.update deploy` **To Update Userbot.**",
                reply_to_message_id=status.id,
            )
            remove("output.txt")
        else:
            await status.edit(
                f"\n`Your BOT is`  **up-to-date**  `with branch`  **[{ac_br}]**\n",
                disable_web_page_preview=True,
            )
            repo.__del__()
            return
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if not HEROKU_APP_NAME:
            await status.edit(
                "`Please set up the HEROKU_APP_NAME variable to be able to update userbot.`"
            )
            repo.__del__()
            return
        heroku_app = next(
            (
                app
                for app in heroku_applications
                if app.name == HEROKU_APP_NAME
            ),
            None,
        )
        if heroku_app is None:
            await status.edit(
                f"{txt}\n`Invalid Heroku credentials for updating userbot dyno.`"
            )
            repo.__del__()
            return
        await status.edit(
            "`[HEROKU]: Pertamax Userbot Penyebaran Pembaruan sedang berlangsung...`"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", f"https://api:{HEROKU_API_KEY}@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except GitCommandError:
            pass
        await status.edit(
            "`Pertamax Userbot Berhasil diperbarui! Userbot dapat digunakan kembali.`"
        )
    else:
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await updateme_requirements()
        await status.edit(
            "`HyperRobot Berhasil diperbarui! Userbot dapat digunakan kembali.`",
        )
        args = [sys.executable, "-m", "ling"]
        execle(sys.executable, *args, environ)
        return


@Client.on_message(filters.command("youpdate", cmd) & filters.me)
async def updatees(client: Client, message: Message):
    if await is_heroku() and HAPP is None:
        return await message.edit_text(
            "Make sure your HEROKU_API_KEY and HEROKU_APP_NAME are configured correctly in heroku config vars",
        )
    response = await message.edit_text("Checking for available updates...")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit("Invalid Git Repsitory")
    to_exc = f"git fetch origin {BRANCH} &> /dev/null"
    await bash(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("Bot is up-to-date!")
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    updates = "".join(
        f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Commited on:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
        for info in repo.iter_commits(f"HEAD..origin/{BRANCH}")
    )
    _update_response_ = "<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await PasteBin(updates)
        nrs = await response.edit(
            f"<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n[Click Here to checkout Updates]({url})"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    await bash("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            await response.edit(
                f"{nrs.text}\n\nBot was updated successfully on Heroku! Now, wait for 2 - 3 mins until the bot restarts!"
            )
            await bash(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            return await response.edit(f"{nrs.text}\n\nERROR: <code>{err}</code>")
    else:
        await bash("pip3 install -r requirements.txt")
        restart()
        exit()


@Client.on_message(filters.command("logs", cmd) & filters.me)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    Man = await edit_or_reply(message, "**Sedang Mengambil Logs Heroku**")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="ling/split/Ling.jpg",
        caption="**Ini Logs Heroku Pertamax**",
    )
    await Man.delete()
    remove("Logs-Heroku.txt")


add_command_help(
    "update",
    [
        ["update", "Untuk melihat list pembaruan terbaru dari HyperRobot."],
        ["update deploy", "Untuk mengupdate userbot."],
        ["restart", "Untuk merestart Userbot."],
        ["shotdown", "Untuk Mematikan Userbot."],
    ],
)
