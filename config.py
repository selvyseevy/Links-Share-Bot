# +++ Modified By [telegram username: @Codeflix_Bots
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8707816870:AAESQbyDBhaEj6x3Jyd4t3GxaEMf1h_TJYA")
APP_ID = int(os.environ.get("APP_ID", "8707816870"))
API_HASH = os.environ.get("API_HASH", "2a8d13c1d6ce82476411f003b6922e47")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "8480922250"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://akdanimes_97:akdanimes_97@cluster0.5e3ojhb.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Codeflix_Bots</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Akd_Animess'>ᴀᴋᴅ ᴀɴɪᴍᴇ</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/akd_animes97>ᴀᴋᴅ</a>\n» Our Community: <a href=https://t.me/Akd_hanimee>ᴀᴋᴅ Network</a>\n» Anime Channel: <a href=https://t.me/Akd_Animess>AKD ANIMES</a>\n» Ongoing Anime: <a href=https://t.me/AKD_Ongoing_Animes>Ongoing AKD</a>\n» Developer: <a href=https://t.me/akd_animes97>AKD</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by Yato (@ProYato) to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Akd_hanimee'>ᴀᴋᴅ ʜᴀɴɪᴍᴇ</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/akd_animes_backup'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/akd_animes97'>ᴀᴋᴅ</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @akd_animes97</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/akd_animes_backup'>ᴀᴋᴅ ᴀɴɪᴍᴇꜱ</a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/AKD_Anime_Movies'>ᴀᴋᴅ ᴍᴏᴠɪᴇꜱ  sᴘᴏᴛ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/Akd_Webseries'>ᴡᴇʙsᴇʀɪᴇs</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Hanime_backup'>ʜᴀɴɪᴍᴇ ʜɪɴᴅɪ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/AKD_Manhwa'>ᴘᴏʀɴʜᴡᴀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Akd_hanimee'>ᴀᴋᴅ ʜᴀɴɪᴍᴇ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @akd_animes97</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!
#--- ---- ---- ---#Auto approve --- --- - -- -  - - - - - - - - - - - --  - -

# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003773420091")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "8480922250").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(8480922250)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
