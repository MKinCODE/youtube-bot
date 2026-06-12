from dotenv import load_dotenv

from agents.script_generator import ScriptGenerator
from agents.topic_finder import TopicFinder

load_dotenv()

topic_finder = TopicFinder()

topic = topic_finder.get_topic()

print("\n" + "=" * 50)
print(f"TOPIC: {topic}")
print("=" * 50 + "\n")

generator = ScriptGenerator()

script = generator.generate(topic)

print(script)