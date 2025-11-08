# Basic rate-limit/backoff
import asyncio

async def backoff_retry(fn, *args, retries: int = 3):
    delay = 1
    for i in range(retries):
        try:
            return await fn(*args)
        except Exception:
            await asyncio.sleep(delay)
            delay *= 2
    raise
