import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    API_KEY = os.getenv("ANTHROPIC_API_KEY")
    MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4000"))

    @staticmethod
    def validate():
        if not Config.API_KEY:
            raise ValueError("ANTHROPIC_API_KEY is missing")


Config.validate()