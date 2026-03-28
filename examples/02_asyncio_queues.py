import asyncio
import random

async def producer(queue: asyncio.Queue, count: int):
    for i in range(1, count+1):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        data = f"item-{i}"
        await queue.put(data)
        print(f"[PRODUCER] Produced {data}")
    await queue.put(None)  # sentinel

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            await queue.put(None)  # передаем сигнал другим потребителям
            break
        await asyncio.sleep(random.uniform(0.1, 1.0))
        print(f"[CONSUMER] Consumed {item}")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue, 5),
        consumer(queue)
    )

asyncio.run(main())