# Data fetching and processing
import httpx

async def fetch_profile(api_url: str):
    # call external social API; wrap with retries in later step
    async with httpx.AsyncClient() as c:
        r = await c.get(api_url)
        return r.json()

def engagement_rate(likes:int, comments:int, followers:int):
    if not followers:
        return 0.0
    return (likes + comments) / followers
