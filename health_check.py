import aiohttp
import asyncio

VMs = [
    "http://127.0.0.1:8000/ping",
    "http://127.0.0.1:8000/health"
]

async def check_health(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            return f"{url} → {response.status}"
    except Exception as e:
        return f"{url} → ERROR: {e}"

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(check_health(session, vm) for vm in VMs))
        for r in results:
            print(r)

asyncio.run(main())

