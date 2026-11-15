import asyncio
from src.engine.worker import probe_single

async def run_probe_batch(session, url: str, count: int):
    tasks = [probe_single(session, url) for _ in range(count)]
    return await asyncio.gather(*tasks)
