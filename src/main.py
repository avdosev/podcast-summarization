import asyncio
import ya_music

async def amain():
    # await ya_music.test()
    await ya_music.download_track('https://music.yandex.ru/album/9294155/track/120577990')
    pass

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(amain())
    except KeyboardInterrupt:
        pass