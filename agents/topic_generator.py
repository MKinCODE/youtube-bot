from groq import Groq
import os


class TopicGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_topics(self):
        prompt = """
        Generate 50 YouTube Shorts topics.
        
        Niche:
        Companies and Human Psychology
        
        50% of topics must be company stories.
        50% of topics must be human psychology.
        
        Good examples:
        
        How Nvidia Became a Trillion Dollar Company
        Why Apple Users Never Switch
        The Rise and Fall of WeWork
        Why People Buy Luxury Watches
        How Starbucks Conquered the World
        Why Humans Love Status Symbols
        Why Nokia Failed
        How OpenAI Became Famous
        
        Rules:
        - One topic per line
        - No numbering
        - No quotes
        - No generic topics
        - No academic sounding topics
        - No words like "unlocking", "understanding", "exploring"
        - Make every topic feel clickable
        - Maximum 10 words per topic
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

        topics = response.choices[0].message.content.split("\n")

        topics = [
            topic.strip()
            for topic in topics
            if topic.strip()
        ]

        return topics