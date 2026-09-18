import json
from qa_pipeline.tools.llm_client import ClaudeClient
from qa_pipeline.tools.utils import extract_json

class TestGenerator:

    def __init__(self):
        self.llm = ClaudeClient()

    def generate(self, requirement_text: str):

        prompt = f"""
You are a Senior QA Engineer.

Generate 5 test cases in STRICT JSON format.

Requirement:
{requirement_text}
"""

        response = self.llm.ask(prompt)
        #print(response);
        return extract_json(response)