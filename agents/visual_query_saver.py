from pathlib import Path
from datetime import datetime


class VisualQuerySaver:
    def __init__(self):
        self.output_dir = Path(
            "output/visual_queries"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, topic, queries):
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
            f.write(queries)

        return filepath