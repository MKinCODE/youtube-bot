from pathlib import Path
from datetime import datetime


class AudioSaver:
    def __init__(self):
        self.output_dir = Path("output/audio")
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def get_path(self, topic):
        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        safe_topic = (
            topic.replace(" ", "_")
            .replace("/", "_")
        )

        return str(
            self.output_dir /
            f"{timestamp}_{safe_topic}.mp3"
        )