import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 21968859

API_HASH = "21a59d21687f01d448530ee88a26b1eb"

BOT_TOKEN = "8309548271:AAHvN4f9aeDvBHRHCbDQ9WI3AHmiZuCMhdQ"

BOT_ID = 8309548271

BOT_USERNAME = "@CelaviraBot"

OWNER_USERNAME = "@eren_aethonix"

BOT_NAME = "𝐂𝐞𝐥𝐚𝐯𝐢𝐫𝐚 ꭙ 𝐌ᴜsɪᴄ 🌹"

ASSUSERNAME = "@Celaviraassistant"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://thebiggestcomebackever:EREN1234@cluster0.7q7ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", "-1002346695101"))

DISASTER_LOG = -1002346695101

OWNER_ID = 7774827065

SPECIAL_USER = 7774827065

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/aethonixsupport"

SUPPORT_CHAT = "https://t.me/igrischatsupport"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "BQE71UwAATI360lN5tLXm18OD4UCPh8rHh6FwARnhWfQV0N4HWH0prMrd5cF0VQQfoOyQMRI3U6cg_kL0Q2UiA6AVVSnvLbjqss7eWCO4cu4dMFdMq_pGVoqlx_8_wrejw5N6zsl6tD7925snZcwugdXt_TlRZ9OVERGWbcTcX8OtkRc9uqkMCWWYgt3UWIc5iI7KFi6iQs9mD5t07QIELAHdQ-61rot8GPAM37ZGNutVJbEkeo-tayg6egl4TgMcVj88i0778bw69WDBXptXIH6v2coHUBw6AZ8ElH8Pn-17BgFMRpZdbo-zvX1-JL-UuARb1QIMWsn_kXj4vpmhNG-iCUNnwAAAAG072FsAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
STATS_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
STREAM_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/xShCWv4S/photo-2025-08-02-13-48-10-7533984627074007064.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
