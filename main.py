from dotenv import load_dotenv

from agents.topic_finder import TopicFinder
from agents.script_generator import ScriptGenerator
from agents.script_saver import ScriptSaver

load_dotenv()

topic_finder = TopicFinder()
generator = ScriptGenerator()
saver = ScriptSaver()

topic = topic_finder.get_topic()

print("\n" + "=" * 50)
print(f"TOPIC: {topic}")
print("=" * 50 + "\n")

script = generator.generate(topic)

filepath = saver.save(topic, script)

print(script)

print("\nSaved to:")
print(filepath)