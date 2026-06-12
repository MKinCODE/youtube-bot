from groq import Groq
import os


class VisualPlanner:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, topic, script):
        prompt = f"""
You are a YouTube Shorts video editor.

TOPIC:
{topic}

SCRIPT:
{script}

Create a shot list.

Requirements:

- 8 to 12 shots
- One shot per line
- Short descriptions
- Visual only
- No narration
- No timestamps
- Focus on stock footage style visuals

Examples:

Apple Store exterior
Person using iPhone
MacBook and AirPods on desk
Crowded shopping mall
Tesla factory robots
Nvidia headquarters

Output only the shot list.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content