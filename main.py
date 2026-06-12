from dotenv import load_dotenv

from agents.topic_finder import TopicFinder
from agents.research_agent import ResearchAgent
from agents.script_generator import ScriptGenerator
from agents.script_saver import ScriptSaver
from agents.research_saver import ResearchSaver

load_dotenv()

topic_finder = TopicFinder()

research_agent = ResearchAgent()
research_saver = ResearchSaver()

script_generator = ScriptGenerator()
script_saver = ScriptSaver()

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

print("\nRESEARCH\n")
print(research)

print("\nSCRIPT\n")
print(script)

print("\nSaved Research:")
print(research_path)

print("\nSaved Script:")
print(script_path)