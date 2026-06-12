from groq import Groq
import os

class ScriptGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, topic):
        prompt = f"""
        Write a YouTube Shorts narration.
        
        Topic:
        {topic}
        
        Requirements:
        
        - 45-60 seconds
        - Start with a strong hook
        - Simple conversational English
        - Explain the idea clearly
        - Build curiosity every few sentences
        - End with a memorable conclusion
        
        IMPORTANT:
        
        - Do NOT invent statistics
        - Do NOT invent studies
        - Do NOT invent percentages
        - Do NOT invent quotes
        - Do NOT invent facts
        
        If you are uncertain about a fact, explain the idea instead.
        
        Avoid phrases like:
        "Studies show"
        "Researchers found"
        "90% of people"
        "Experts say"
        
        unless you actually know the source.
        
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