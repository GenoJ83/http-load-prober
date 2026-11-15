from pydantic import BaseModel

class RequestResult(BaseModel):
    status_code: int
    latency_ms: float
    bytes_received: int
    error: str = None
