import aiohttp
from config import API_URL
import json

async def check_nrk(nrk: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            payload = {"nrk": nrk} 
            async with session.post(f"{API_URL}", data=payload) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        formatted_response = json.loads(response_text)
                        return formatted_response
                    except json.JSONDecodeError:
                        return None
                else:
                    return None 
    except aiohttp.ClientError:
        return None
    except Exception:
        return None