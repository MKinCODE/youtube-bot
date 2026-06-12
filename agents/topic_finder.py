import json
from pathlib import Path

from agents.topic_generator import TopicGenerator


class TopicFinder:
    def __init__(self):
        self.used_topics_file = Path("data/used_topics.json")

        if not self.used_topics_file.exists():
            self.used_topics_file.write_text("[]")

        self.topic_generator = TopicGenerator()

    def load_used_topics(self):
        with open(self.used_topics_file, "r") as f:
            return json.load(f)

    def save_used_topic(self, topic):
        used_topics = self.load_used_topics()

        used_topics.append(topic)

        with open(self.used_topics_file, "w") as f:
            json.dump(used_topics, f, indent=4)

    def get_topic(self):
        used_topics = self.load_used_topics()

        generated_topics = self.topic_generator.generate_topics()

        available_topics = [
            topic
            for topic in generated_topics
            if topic not in used_topics
        ]

        if not available_topics:
            raise Exception("No new topics available")

        topic = available_topics[0]

        self.save_used_topic(topic)

        return topic