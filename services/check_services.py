import aiohttp
from config import API_URL
import json
import subprocess

async def check_nrk(nrk: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            payload = {"nrk": nrk} 
            async with session.post(f"{API_URL}", data=payload) as response:
                if response.status == 200:
                    formatted_response = json.loads(response.text)
                    formatted_response_str = json.dumps(formatted_response, indent=2)
                    jq_process = subprocess.Popen(['jq', '.'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
                    jq_output, _ = jq_process.communicate(input=formatted_response_str)
                    return await jq_output
                else:
                    return None 
    except Exception:
        return None 
