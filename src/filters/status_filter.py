from typing import List
from src.models.result import RequestResult

def filter_by_status(results: List[RequestResult], status: int) -> List[RequestResult]:
    return [r for r in results if r.status_code == status]
