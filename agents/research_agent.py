from groq import Groq
import os


class ResearchAgent:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def research(self, topic):
        prompt = f"""
You are a research assistant.

Topic:
{topic}

Give:

- 5 important facts
- key people involved
- important events
- important products/services

Rules:
- concise
- bullet points only
- no explanations
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