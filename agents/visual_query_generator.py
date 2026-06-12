from groq import Groq
import os


class VisualQueryGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, topic, visual_plan):
        prompt = f"""
TOPIC:
{topic}

VISUAL PLAN:
{visual_plan}

Convert each shot into a highly searchable image/video query.

Rules:

- One query per line
- No numbering
- No explanations
- Be specific
- Search-engine friendly

Example:

Tesla Gigafactory aerial view

Elon Musk keynote presentation

Tesla Model S highway driving

Supercharger station at night
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