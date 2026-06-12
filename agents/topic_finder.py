import json
import random
from pathlib import Path


class TopicFinder:
    def __init__(self):
        self.used_topics_file = Path("data/used_topics.json")
        self.topics_file = Path("data/topics.json")

        if not self.used_topics_file.exists():
            self.used_topics_file.write_text("[]")

    def load_used_topics(self):
        with open(self.used_topics_file, "r") as f:
            return json.load(f)

    def save_used_topic(self, topic):
        used_topics = self.load_used_topics()

        used_topics.append(topic)

        with open(self.used_topics_file, "w") as f:
            json.dump(used_topics, f, indent=4)

    def get_topic(self):
        with open(self.topics_file, "r") as f:
            all_topics = json.load(f)

        used_topics = self.load_used_topics()

        available_topics = [
            topic
            for topic in all_topics
            if topic not in used_topics
        ]

        if not available_topics:
            raise Exception("No topics left")

        topic = random.choice(available_topics)

        self.save_used_topic(topic)

        return topic