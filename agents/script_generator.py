from groq import Groq
import os


class ScriptGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, topic, research):
        prompt = f"""
You are writing a viral YouTube Shorts narration.

TOPIC:
{topic}

RESEARCH:
{research}

Your job is NOT to list facts.

Your job is to tell a story.

Structure:

1. Strong hook
2. Introduce conflict/problem
3. Reveal turning point
4. End with payoff or insight

Requirements:

- 45-60 seconds
- Short sentences
- Conversational English
- High curiosity
- Sound like a successful Shorts creator
- Use research facts naturally

Rules:

- Never start with "Imagine"
- Never start with a question
- Never sound like Wikipedia
- Never list facts one after another
- Do not use bullet points
- Do not use headings

Bad Example:

"Google was founded in 1998.
It launched AdWords in 2000.
It acquired YouTube in 2006."

Good Example:

"Google wasn't the first search engine.

But it became the biggest.

While everyone else focused on finding websites,
Google figured out how to make money from attention.

That decision changed the internet forever."

Narration only.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content