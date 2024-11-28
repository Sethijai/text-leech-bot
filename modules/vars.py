import os

API_ID    = os.environ.get("API_ID", "23713783")
API_HASH  = os.environ.get("API_HASH", "2daa157943cb2d76d149c4de0b036a99")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7853203368:AAE801naC4GMeyrkEfyflPItRwMvLmQddPY") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8800))  # Default to 8000 if not set
