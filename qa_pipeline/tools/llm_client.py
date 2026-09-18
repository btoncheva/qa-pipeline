from anthropic import Anthropic
from qa_pipeline.config import Config


class ClaudeClient:

    def __init__(self):
        self.client = Anthropic(api_key=Config.API_KEY)

    def ask(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=Config.MODEL,
            max_tokens=Config.MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text