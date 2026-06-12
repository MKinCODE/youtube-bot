from groq import Groq
import os


class CriticAgent:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def review(self, topic, script):
        prompt = f"""
You are a YouTube Shorts growth expert.

TOPIC:
{topic}

SCRIPT:
{script}

Review this script.

Score each category from 1-10:

- Hook
- Curiosity
- Storytelling
- Retention Potential
- Virality Potential

Then provide:

- Overall Score
- Biggest Weakness
- One Improvement Suggestion

If Overall Score is below 8:
Rewrite only the hook.

Keep response concise.
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