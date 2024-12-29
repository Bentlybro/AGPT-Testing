import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TEMP_DOWNLOAD_PATH = "temp_downloads"