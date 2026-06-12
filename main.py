from dotenv import load_dotenv
from agents.script_generator import ScriptGenerator

load_dotenv()

generator = ScriptGenerator()

script = generator.generate(
    "How Nvidia became a trillion dollar company"
)

print(script)