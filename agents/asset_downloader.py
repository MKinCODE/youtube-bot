import os
import requests
from pathlib import Path


class AssetDownloader:
    def __init__(self):
        self.api_key = os.getenv("PEXELS_API_KEY")

        self.headers = {
            "Authorization": self.api_key
        }

        self.output_dir = Path("output/assets")
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def download_first_video(self, query):
        url = (
            "https://api.pexels.com/videos/search"
            f"?query={query}&per_page=1"
        )

        response = requests.get(
            url,
            headers=self.headers
        )

        data = response.json()

        if not data.get("videos"):
            return None

        video = data["videos"][0]

        video_url = video["video_files"][0]["link"]

        filename = (
            query.replace(" ", "_")
            + ".mp4"
        )

        filepath = (
            self.output_dir / filename
        )

        video_data = requests.get(
            video_url
        )

        with open(filepath, "wb") as f:
            f.write(video_data.content)

        return str(filepath)