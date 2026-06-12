from dotenv import load_dotenv

from agents.asset_downloader import (
    AssetDownloader
)

load_dotenv()

downloader = AssetDownloader()

path = downloader.download_first_video(
    "business meeting office"
)

print(path)