from pydantic import BaseModel

class IncidentCreate(BaseModel):
    service: str
    severity: str
    exception: str
    endpoint: str
    stack_trace: str