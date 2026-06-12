from dotenv import load_dotenv

from agents.topic_finder import TopicFinder
from agents.research_agent import ResearchAgent
from agents.research_saver import ResearchSaver
from agents.script_generator import ScriptGenerator
from agents.script_saver import ScriptSaver
from agents.voice_generator import VoiceGenerator
from agents.audio_saver import AudioSaver

import asyncio

load_dotenv()

topic_finder = TopicFinder()

research_agent = ResearchAgent()
research_saver = ResearchSaver()

script_generator = ScriptGenerator()
script_saver = ScriptSaver()

voice_generator = VoiceGenerator()
audio_saver = AudioSaver()

topic = topic_finder.get_topic()

print("\n" + "=" * 50)
print(f"TOPIC: {topic}")
print("=" * 50 + "\n")

research = research_agent.research(topic)

research_path = research_saver.save(
    topic,
    research
)

script = script_generator.generate(
    topic,
    research
)

script_path = script_saver.save(
    topic,
    script
)

audio_path = audio_saver.get_path(
    topic
)

asyncio.run(
    voice_generator.generate(
        script,
        audio_path
    )
)

print("\nSaved Research:")
print(research_path)

print("\nSaved Script:")
print(script_path)

print("\nSaved Audio:")
print(audio_path)