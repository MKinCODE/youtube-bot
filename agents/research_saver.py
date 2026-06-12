from pathlib import Path
from datetime import datetime


class ResearchSaver:
    def __init__(self):
        self.output_dir = Path("output/research")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save(self, topic, research):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        safe_topic = topic.replace(" ", "_")
        safe_topic = safe_topic.replace("/", "_")

        filename = f"{timestamp}_{safe_topic}.txt"

        filepath = self.output_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(research)

        return filepath