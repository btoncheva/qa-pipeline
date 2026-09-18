from qa_pipeline.tools.llm_client import ClaudeClient


class FailureAnalyzer:

    def __init__(self):
        self.llm = ClaudeClient()

    def analyze(self, failure_text: str):

        prompt = f"""
You are a Senior QA Engineer.

Analyze failure and return:
- root cause
- severity
- confidence

Failure:
{failure_text}
"""

        return self.llm.ask(prompt)