import logging
import os
import constants
from pathlib import Path
from pyrogram import Client
from pyrogram.session import StringSession

# --- Environment Variable Check ---
# Get the session string from environment variables.
# This is the correct way to handle sensitive data in production.
SESSION_STRING = os.getenv("SESSION_STRING")
if not SESSION_STRING:
    raise ValueError("SESSION_STRING environment variable is not set!")

# --- Project Constants (assuming these exist in a constants.py file) ---
# If you don't have a constants.py or don't need a WORK_DIRPATH,
# you can define DATA_FILEPATH directly.
WORK_DIRPATH = Path(__file__).parent 

# --- Telegram API Credentials (from my.telegram.org) ---
API_ID = 24795920
API_HASH = "9445a5dfa20c3abe79ee7657f14f3a8b"

# --- Userbot Session ---
SESSION_NAME = "gifts_notifier_session"

# --- Bot Tokens (for sending notifications) ---
# Get tokens from BotFather (@BotFather on Telegram) for your notification bots.
BOT_TOKENS = [
    "7430380189:AAG8XSxj5BqQM2OydnNFAVHELv0OJisxOYI",
    "7070072951:AAH1KF-9Z3yvYQxsy4YUVvtljvxFATwyJJ4",
    "7954664840:AAHNss3PmdieuEePXtfEYqTTwlzenl_fvYE",
    "8097489642:AAGvWSmyIX1jV095O61f2nSxeSTJi3R9mD8"
]

# --- Notification Chat IDs ---
NOTIFY_CHAT_ID = -4877488229 
NOTIFY_UPGRADES_CHAT_ID = None

# --- Operational Settings ---
CHECK_INTERVAL = 180.0
CHECK_UPGRADES_PER_CYCLE = 5.0
HTTP_REQUEST_TIMEOUT = 30.0

# --- Data Persistence Settings ---
DATA_FILEPATH = constants.WORK_DIRPATH / "star_gifts.json"
DATA_SAVER_DELAY = 2.0

# --- Logging Settings ---
TIMEZONE = "Asia/Kolkata"
CONSOLE_LOG_LEVEL = logging.DEBUG
FILE_LOG_LEVEL = logging.INFO
LOG_LEVEL = "INFO"

# --- Notification Display Text Formats ---
NOTIFY_TEXT = """\
{title}

№ {number} (<code>{id}</code>)
{total_amount}{available_amount}{sold_out}
💎 Price: {price} ⭐️
♻️ Convert price: {convert_price} ⭐️
"""

NOTIFY_TEXT_TITLES = {
    True: "🔥 A new limited gift has appeared",
    False: "❄️ A new gift has appeared"
}

NOTIFY_TEXT_TOTAL_AMOUNT = "\n🎯 Total amount: {total_amount}"
NOTIFY_TEXT_AVAILABLE_AMOUNT = "\n❓ Available amount: {available_amount} ({same_str}{available_percentage}%, updated at {updated_datetime} UTC)\n"
NOTIFY_TEXT_SOLD_OUT = "\n⏰ Completely sold out in {sold_out}\n"

NOTIFY_UPGRADES_TEXT = "Gift is upgradable! (<code>{id}</code>)"

# --- Delays for Notifications ---
NOTIFY_AFTER_STICKER_DELAY = 5.0
NOTIFY_AFTER_TEXT_DELAY = 6.0

# --- Gift Notification Filters (from your provided data) ---
MIN_PRICE_STARS = 100
MAX_PRICE_STARS = 500
MAX_SUPPLY_LIMIT = 50
NOTIFY_COLLECTIBLE_GIFTS_ONLY = False
NOTIFY_UPGRADABLE_GIFTS_ONLY = False
NOTIFY_LIMITED_GIFTS_ONLY = False
BLACKLIST_GIFT_IDS = []
