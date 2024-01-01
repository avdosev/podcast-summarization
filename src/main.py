import asyncio
import ya_music
import speech2text
import pprint
from summarize import summarize
import rest_parser

interests = [
    'https://music.yandex.ru/album/9294155/track/60856985',
    'https://music.yandex.ru/album/9294155/track/68197581',
    'https://music.yandex.ru/album/9294155/track/68518006',
    'https://music.yandex.ru/album/9294155/track/68866563',
    'https://music.yandex.ru/album/9294155/track/69172026',
    'https://music.yandex.ru/album/9294155/track/69964578',
    'https://music.yandex.ru/album/9294155/track/73821990',
    'https://music.yandex.ru/album/9294155/track/81028981',
    'https://music.yandex.ru/album/9294155/track/84989874',
    'https://music.yandex.ru/album/9294155/track/94056928',
    'https://music.yandex.ru/album/9294155/track/94949844',
    'https://music.yandex.ru/album/9294155/track/99948283',
    'https://music.yandex.ru/album/9294155/track/100458776',
    'https://music.yandex.ru/album/9294155/track/100802824',
    'https://music.yandex.ru/album/9294155/track/101849508',
    'https://music.yandex.ru/album/9294155/track/102072454',
    'https://music.yandex.ru/album/9294155/track/102694626',
    'https://music.yandex.ru/album/9294155/track/103834394',
    'https://music.yandex.ru/album/9294155/track/105405843',
    'https://music.yandex.ru/album/9294155/track/105856544',
    'https://music.yandex.ru/album/9294155/track/108034688',
    'https://music.yandex.ru/album/9294155/track/108210691',
    'https://music.yandex.ru/album/9294155/track/108533666',
    'https://music.yandex.ru/album/9294155/track/109445652',
    'https://music.yandex.ru/album/9294155/track/109732836',
    'https://music.yandex.ru/album/9294155/track/110006036',
    'https://music.yandex.ru/album/9294155/track/111958424',
    'https://music.yandex.ru/album/9294155/track/120577990',
]

async def amain():
    # await ya_music.test()
    for track_url in interests[:4]:
        track_info = rest_parser.parse(track_url)
        filename = await ya_music.download_track(track_url)
        text = speech2text.transcribe(filename)
        print(await summarize(text, cache_key=f"tmp/summary/{track_info['album']}/{track_info['track']}"))

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(amain())
    except KeyboardInterrupt:
        pass
