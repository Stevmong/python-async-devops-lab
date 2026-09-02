import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch(session, "https://example.com"),
            fetch(session, "https://httpbin.org/get")
        )
        print([len(r) for r in results])  # print response sizes

asyncio.run(main())

