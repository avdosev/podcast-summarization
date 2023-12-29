import time
import logging
import aiohttp
import asyncio
from config import read_config

logger = logging.getLogger(__name__)

endpoint = 'https://300.ya.ru/api/text-summary'
api_key = read_config()['300_token']

async def get_summary(text) -> list[str] | None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                endpoint, 
                json={'text': text}, 
                headers={'Authorization': 'OAuth '+api_key, 'Content-Type': 'application/json'},
            ) as resp:
                res = await resp.json()
                print(f'status: {resp.status}, response: {res}')
    
        return res['thesis']
    except:
        return None

def split_to_chunks(text: str) -> list[str]:
    pass

async def summarize(text: str):
    return ' '.join(get_summary(text))