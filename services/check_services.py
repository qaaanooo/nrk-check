import aiohttp
from config import API_URL

async def check_nrk(nrk: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            data = {"nrk": nrk} 
            async with session.post(f"{API_URL}", json=data) as response:
                if response.status == 200:
                    return await response.json() 
                else:
                    return None 
    except Exception:
        return None 
