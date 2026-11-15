import asyncio

class WorkerPool:
    def __init__(self, concurrency: int = 10):
        self.sem = asyncio.Semaphore(concurrency)
    async def execute(self, coro):
        async with self.sem:
            return await coro
