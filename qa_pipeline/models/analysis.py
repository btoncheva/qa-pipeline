from pydantic import BaseModel


class FailureAnalysis(BaseModel):
    root_cause: str
    severity: str
    confidence: str