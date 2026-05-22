from dotenv import load_dotenv
from google import genai

class AiBot:
    def __init__(self) -> None:
        load_dotenv()
        self.client = genai.Client()

    def generate_text(
        self,
        prompt,
        model="gemini-2.5-flash"
    ):
        response = self.client.models.generate_content(
            model=model,
            contents=prompt
        )
        return response
