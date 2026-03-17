import asyncio

async def slow_task():
    await asyncio.sleep(2)
    return "Медленный"

async def fast_task():
    await asyncio.sleep(1)
    return "Быстрый"

async def main():
    results = await asyncio.gather(
    slow_task(),  # Передаем медленную первой
    fast_task()   # Передаем быструю второй
    )
    print(results)

asyncio.run(main())