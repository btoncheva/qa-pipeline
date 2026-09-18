from pydantic import BaseModel


class TestCase(BaseModel):
    id: str
    title: str
    preconditions: list[str]
    steps: list[str]
    expected_result: str