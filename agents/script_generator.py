from groq import Groq
import os


class ScriptGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, topic, research):
        prompt = f"""
Write a YouTube Shorts narration.

TOPIC:
{topic}

RESEARCH:
{research}

Requirements:

- 45-60 seconds
- Start with a strong statement
- Never start with "Imagine"
- Never start with a question
- Use the research information
- Focus on story, conflict, or insight
- Short sentences
- Simple English
- Build curiosity naturally
- End with a memorable conclusion

Rules:

- Do NOT invent statistics
- Do NOT invent studies
- Do NOT invent percentages
- Do NOT invent quotes
- Do NOT invent facts

Only use information from the research section.

No bullet points.
No headings.
Narration only.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content