from pathlib import Path

from qa_pipeline.tools.generator import TestGenerator
from qa_pipeline.tools.analyzer import FailureAnalyzer


class QAPipeline:

    def __init__(self):
        self.generator = TestGenerator()
        self.analyzer = FailureAnalyzer()

    def generate_tests(self, file_path: str):
        text = Path(file_path).read_text()
        return self.generator.generate(text)

    def analyze_failure(self, file_path: str):
        text = Path(file_path).read_text()
        return self.analyzer.analyze(text)