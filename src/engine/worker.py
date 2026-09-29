import time
from src.models.result import RequestResult

async def probe_single(session, url: str) -> RequestResult:
    t0 = time.perf_counter()
    try:
        async with session.get(url) as resp:
            body = await resp.read()
            lat = (time.perf_counter() - t0) * 1000
            return RequestResult(status_code=resp.status, latency_ms=round(lat, 2), bytes_received=len(body))
    except Exception as e:
        lat = (time.perf_counter() - t0) * 1000
        return RequestResult(status_code=0, latency_ms=round(lat, 2), bytes_received=0, error=str(e))
