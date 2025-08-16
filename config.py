import logging
import os
import constants
from pathlib import Path
SESSION_NAME = "account"
# --- Project Constants (assuming these exist in a constants.py file) ---
# If you don't have a constants.py or don't need a WORK_DIRPATH,
# you can define DATA_FILEPATH directly.
# Example: WORK_DIRPATH = Path(__file__).parent
# Or for your case, based on your provided data, a simple string path is fine.
# We'll define a default WORK_DIRPATH for data persistence.
WORK_DIRPATH = Path(__file__).parent # This assumes config.py is in the root of the project

# --- Telegram API Credentials (from my.telegram.org) ---
# You MUST replace these with your own API ID and API HASH.
API_ID = 24795920  # Replace with your actual API ID
API_HASH = "9445a5dfa20c3abe79ee7657f14f3a8b"  # Replace with your actual API HASH

# --- Userbot Session ---
# A name for the Pyrogram session file. This file will store your userbot's
# session so it doesn't have to log in every time.
SESSION_NAME = "gifts_notifier_session"

# --- Bot Tokens (for sending notifications) ---
# Get tokens from BotFather (@BotFather on Telegram) for your notification bots.
# This project uses multiple bots for robustness.
BOT_TOKENS = [
    "7430380189:AAG8XSxj5BqQM2OydnNFAVHELv0OJisxOYI", # !!! IMPORTANT: Replace with your actual bot token(s) !!!
    "7070072951:AAH1KF-9Z3yvYQxsy4YUVvtljvxFATwyJJ4",
    "7954664840:AAHNss3PmdieuEePXtfEYqTTwlzenl_fvYE",
    "8097489642:AAGvWSmyIX1jV095O61f2nSxeSTJi3R9mD8"
]

# --- Notification Chat IDs ---
# The chat ID where the notification bot should send messages for new/updated gifts.
# This is usually your own user ID or a group chat ID where the bot is admin.
NOTIFY_CHAT_ID = -4877488229  # !!! IMPORTANT: Your numerical Telegram user ID or group chat ID for general notifications !!!

# The chat ID for upgrade notifications.
# If you don't need upgrade notifications, set it to `None`.
# Additionally, bots can't check upgrades for gifts, Telegram will raise [400 BOT_METHOD_INVALID]
# if you try to use a bot for this. This typically requires a userbot (your main account).
NOTIFY_UPGRADES_CHAT_ID = None  # Set to your chat ID if you need upgrade notifications, e.g., -1002751596218

# --- Operational Settings ---
CHECK_INTERVAL = 180.0  # Time (in seconds) between checks for new gifts. (CHECK_INTERVAL_SECONDS from your data)
CHECK_UPGRADES_PER_CYCLE = 5.0 # Time (in seconds) between checks for upgradable gifts.
HTTP_REQUEST_TIMEOUT = 30.0  # Timeout for HTTP requests (e.g., for notification bot API calls). (HTTP_REQUEST_TIMEOUT_SECONDS from your data)

# --- Data Persistence Settings ---
# Path to the file where detected gift data will be stored to avoid repeat notifications.
# Using Path for better OS compatibility.
DATA_FILEPATH = constants.WORK_DIRPATH / "star_gifts.json" # Adjust if your data file should be elsewhere
DATA_SAVER_DELAY = 2.0  # Delay (in seconds) before saving data to the file after changes. (DATA_SAVE_DELAY_SECONDS from your data)

# --- Logging Settings ---
TIMEZONE = "Asia/Kolkata" # Timezone for logging timestamps. You can change this to your local timezone, e.g., "Asia/Kolkata"
CONSOLE_LOG_LEVEL = logging.DEBUG # Set the logging level for console output
FILE_LOG_LEVEL = logging.INFO # Set the logging level for file output
LOG_LEVEL = "INFO" # This seems redundant with CONSOLE_LOG_LEVEL/FILE_LOG_LEVEL, but keeping it if other parts of your code use it.
# You can map your LOG_LEVEL string to logging constants if needed:
# LOG_LEVEL_MAP = {
#     "DEBUG": logging.DEBUG,
#     "INFO": logging.INFO,
#     "WARNING": logging.WARNING,
#     "ERROR": logging.ERROR,
#     "CRITICAL": logging.CRITICAL,
# }
# CONSOLE_LOG_LEVEL = LOG_LEVEL_MAP.get(LOG_LEVEL, logging.INFO) # Example of mapping

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
NOTIFY_AFTER_STICKER_DELAY = 5.0 # Delay after sending a sticker before sending text
NOTIFY_AFTER_TEXT_DELAY = 6.0    # Delay after sending text notification

# --- Gift Notification Filters (from your provided data) ---
MIN_PRICE_STARS = 100
MAX_PRICE_STARS = 500
MAX_SUPPLY_LIMIT = 50
NOTIFY_COLLECTIBLE_GIFTS_ONLY = False
NOTIFY_UPGRADABLE_GIFTS_ONLY = False
NOTIFY_LIMITED_GIFTS_ONLY = False
BLACKLIST_GIFT_IDS = []

# PHONE_NUMBER is not directly used in the `detector.py`'s `Client` initialization,
# as it appears to rely on `SESSION_NAME` for userbot login.
# However, if your `Client` setup requires it elsewhere, keep it.
# For the `detector.py` shown, it's not explicitly needed in `config.py`.
# PHONE_NUMBER = "+917559818131" # Only if your Pyrogram Client setup requires it.