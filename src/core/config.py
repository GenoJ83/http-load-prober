from pydantic import BaseModel

class LoadConfig(BaseModel):
    target_url: str = 'http://localhost:8000'
    concurrency: int = 10
    duration_seconds: int = 30
    timeout_seconds: float = 5.0
