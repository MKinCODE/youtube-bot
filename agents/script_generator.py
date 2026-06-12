from groq import Groq
import os

class ScriptGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, topic):
        prompt = f"""
        Write a viral YouTube Shorts narration.
        
        Topic:
        {topic}
        
        Rules:
        
        - 45-60 seconds
        - First sentence must be a shocking hook
        - No introductions like "Imagine" or "Did you know"
        - No emojis
        - No bullet points
        - No headings
        - Every sentence should increase curiosity
        - Use simple English
        - End with a surprising fact
        - Sound like a professional YouTube creator
        - Output narration only
        """

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content