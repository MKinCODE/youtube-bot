from dotenv import load_dotenv
import asyncio

from agents.topic_finder import TopicFinder

from agents.research_agent import ResearchAgent
from agents.research_saver import ResearchSaver

from agents.script_generator import ScriptGenerator
from agents.script_saver import ScriptSaver

from agents.visual_planner import VisualPlanner
from agents.visual_plan_saver import VisualPlanSaver

from agents.voice_generator import VoiceGenerator
from agents.audio_saver import AudioSaver


load_dotenv()

topic_finder = TopicFinder()

research_agent = ResearchAgent()
research_saver = ResearchSaver()

script_generator = ScriptGenerator()
script_saver = ScriptSaver()

visual_planner = VisualPlanner()
visual_plan_saver = VisualPlanSaver()

voice_generator = VoiceGenerator()
audio_saver = AudioSaver()

topic = topic_finder.get_topic()

print("\n" + "=" * 50)
print(f"TOPIC: {topic}")
print("=" * 50 + "\n")

# Research
research = research_agent.research(topic)

research_path = research_saver.save(
    topic,
    research
)

# Script
script = script_generator.generate(
    topic,
    research
)

script_path = script_saver.save(
    topic,
    script
)

# Visual Plan
visual_plan = visual_planner.generate(
    topic,
    script
)

visual_plan_path = visual_plan_saver.save(
    topic,
    visual_plan
)

# Voice
audio_path = audio_saver.get_path(
    topic
)

asyncio.run(
    voice_generator.generate(
        script,
        audio_path
    )
)

print("\nRESEARCH\n")
print(research)

print("\nSCRIPT\n")
print(script)

print("\nVISUAL PLAN\n")
print(visual_plan)

print("\nSaved Research:")
print(research_path)

print("\nSaved Script:")
print(script_path)

print("\nSaved Visual Plan:")
print(visual_plan_path)

print("\nSaved Audio:")
print(audio_path)