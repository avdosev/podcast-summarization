from yandex_music import ClientAsync
from config import read_config
import rest_parser 

token = read_config()['yamusic_token']
client = ClientAsync(token)
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
    print(rest_parser.parse(url))

async def _download_track(album, track_id):
    track = await client.tracks([f'{album}:{track_id}'])[0]
    print(track)
    await track.download_track()