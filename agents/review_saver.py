from pathlib import Path
from datetime import datetime


class ReviewSaver:
    def __init__(self):
        self.output_dir = Path(
            "output/reviews"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, topic, review):
        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        safe_topic = (
            topic.replace(" ", "_")
            .replace("/", "_")
        )

        filepath = (
            self.output_dir /
            f"{timestamp}_{safe_topic}.txt"
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(review)

        return filepath