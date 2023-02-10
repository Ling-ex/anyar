from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "👑")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/0a4818429a8a70bb1e8da.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey bro, I am hyper.")
API_HASH = getenv("API_HASH", "be6ba80decab712fe259c55c3cd46b86")
API_ID = getenv("API_ID", "21836949")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001883961446]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_VER = "1.0.3@ling"
BRANCH = getenv("BRANCH", "main") # jangan di ganti kalo ga mau error tolol
CH_SFS = getenv("CH_SFS", "storyQi") # kalo lu mau ganti minimal follow dulu lah kontol
IG_ALIVE = getenv("IG_ALIVE", "rizki.maulna_") # kalo lu mau ganti minimal follow dlu lah kontol
CHANNEL = getenv("CHANNEL", "storyQi") # kalo lu mau ganti minimal follow dulu lah kontol
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "") # optional punya lo ya kontol
GROUP = getenv("GROUP", "HyperSupportQ") # kontol klo lu ganti 
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Ling-ex/anyar")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
