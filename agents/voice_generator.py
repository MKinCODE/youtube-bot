import edge_tts
import asyncio


class VoiceGenerator:
    async def generate(self, text, output_path):
        communicate = edge_tts.Communicate(
            text,
            voice="en-US-GuyNeural"
        )

        await communicate.save(output_path)