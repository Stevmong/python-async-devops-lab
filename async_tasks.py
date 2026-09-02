import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay}s")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1)
    )

asyncio.run(main())

