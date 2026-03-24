
from pydantic import BaseModel
from typing import List

class Log(BaseModel):
    timestamp: str
    system: str
    level: str
    message: str

class AnalysisResponse(BaseModel):
    summary: str
    probable_root_cause: str
    suggested_action: str
