import asyncio

class TokenBucket:
    def __init__(self, rate: int):
        self.rate = rate
        self.tokens = rate
    async def acquire(self):
        await asyncio.sleep(1.0 / self.rate)
