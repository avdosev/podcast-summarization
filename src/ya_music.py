from yandex_music import ClientAsync
from yandex_music.utils.request_async import Request
from config import read_config
import rest_parser 
import os

token = read_config()['yamusic_token']
client = ClientAsync(token, request=Request(timeout=100))
inited = False

async def init():
    global inited
    if not inited: 
        await client.init()
        inited = True

async def test():
    await init()
    print(client.me)
    print()
    result = 'success' if client.me['account']['login'] is not None else 'fail'
    print(result)

async def download_track(url):
    await init()
    info = rest_parser.parse(url)
    return await _download_track(info['album'], info['track'])

async def _download_track(album, track_id):
    filename = f'tmp/music/{album}/{track_id}.mp4'
    if os.path.exists(filename):
        return filename
    
    os.makedirs(f'tmp/music/{album}', exist_ok=True)
    # track = (await client.podcasts(album))
    track = await client.tracks_download_info(f'{track_id}')
    await track[0].downloadAsync(filename)
    return filename
