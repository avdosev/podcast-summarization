import time
import logging
import aiohttp
import asyncio
from config import read_config
import re

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
    sentences = re.split(r'(?<=[!?.]) ')
    max_sentences_in_chunk = 12
    chunks = split_array_chunks(sentences, max_sentences_in_chunk)
    chunks = [' '.join(chunk) for chunk in chunks]

    return chunks


def split_array_chunks(array, chunk_size):
    chunks = []
    for i in range(0, len(array), chunk_size):
        chunk = array[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

async def summarize(text: str):
    chunks = split_to_chunks(text)

    loop = asyncio.get_event_loop()
    tasks = []
    for text in chunks:
        tasks.append(loop.create_task(get_summary(text)))

    summarizations = await asyncio.gather(*tasks)

    return '\n'.join(summarizations)