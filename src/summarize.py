import time
import logging
import aiohttp
import asyncio
from config import read_config
import re
from pathlib import Path


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
                print(f'status: {resp.status}')
                if resp.status != 200:
                    print(await resp.text())
                res = await resp.json()
                # print(f'response: {res}')
                return res['thesis']
    
    except:
        return None

def split_to_chunks(text: str) -> list[str]:
    sentences = re.split(r'(?<=[!?.]) ', text)
    max_sentences_in_chunk = 14
    chunks = split_array_chunks(sentences, max_sentences_in_chunk)
    chunks = [' '.join(chunk) for chunk in chunks]

    return chunks


def split_array_chunks(array, chunk_size):
    chunks = []
    for i in range(0, len(array), chunk_size):
        chunk = array[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

async def summarize(text: str, cache_key = None):
    if cache_key is not None:
        txt_file = Path(cache_key)
        
        if txt_file.exists():
            return txt_file.read_text('utf-8')
    else:
        txt_file = None

    chunks = split_to_chunks(text)

    if len(chunks[-1]) < 300:
        chunks[-2] += chunks[-1]
        chunks.pop()

    summarizations = []

    for chunk_text in chunks:
        summarizations.append(await get_summary(chunk_text))
        await asyncio.sleep(3)

    summarizations = flatten(summarizations)

    summary = '\n'.join(summarizations)

    if txt_file is not None:
        txt_file.parent.resolve().mkdir(parents=True, exist_ok=True)
        txt_file.write_text(summary, 'utf-8')
    
    return summary

def flatten(l):
    return [item for sublist in l for item in sublist]