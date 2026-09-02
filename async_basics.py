import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello async!")

asyncio.run(hello())

