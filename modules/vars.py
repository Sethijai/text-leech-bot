import os

API_ID    = os.environ.get("API_ID", "29626867")
API_HASH  = os.environ.get("API_HASH", "82b19751497d00e47c3032409d130423")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6369798839:AAHoxe7Tli1zJ2yu_Xi2oldn1lJ_MBktLbI") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
