from dotenv import load_dotenv
import asyncio

from agents.topic_finder import TopicFinder

from agents.research_agent import ResearchAgent
from agents.research_saver import ResearchSaver

from agents.script_generator import ScriptGenerator
from agents.script_saver import ScriptSaver

from agents.critic_agent import CriticAgent
from agents.review_saver import ReviewSaver

from agents.visual_planner import VisualPlanner
from agents.visual_plan_saver import VisualPlanSaver

from agents.visual_query_generator import VisualQueryGenerator
from agents.visual_query_saver import VisualQuerySaver

from agents.voice_generator import VoiceGenerator
from agents.audio_saver import AudioSaver

load_dotenv()

topic_finder = TopicFinder()

research_agent = ResearchAgent()
research_saver = ResearchSaver()

script_generator = ScriptGenerator()
script_saver = ScriptSaver()

critic_agent = CriticAgent()
review_saver = ReviewSaver()

visual_planner = VisualPlanner()
visual_plan_saver = VisualPlanSaver()

visual_query_generator = VisualQueryGenerator()
visual_query_saver = VisualQuerySaver()

voice_generator = VoiceGenerator()
audio_saver = AudioSaver()

topic = topic_finder.get_topic()

print("\n" + "=" * 50)
print(f"TOPIC: {topic}")
print("=" * 50 + "\n")

research = research_agent.research(topic)
research_path = research_saver.save(topic, research)

script = script_generator.generate(topic, research)
script_path = script_saver.save(topic, script)

review = critic_agent.review(topic, script)
review_path = review_saver.save(topic, review)

visual_plan = visual_planner.generate(topic, script)
visual_plan_path = visual_plan_saver.save(topic, visual_plan)

visual_queries = visual_query_generator.generate(
    topic,
    visual_plan
)

visual_query_path = visual_query_saver.save(
    topic,
    visual_queries
)

audio_path = audio_saver.get_path(topic)

asyncio.run(
    voice_generator.generate(
        script,
        audio_path
    )
)

print("\nREVIEW\n")
print(review)

print("\nSaved Review:")
print(review_path)