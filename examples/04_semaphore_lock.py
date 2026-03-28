import asyncio
import random

async def worker(worker_id, semaphore):
    async with semaphore:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f"Worker {worker_id} finished")

async def main():
    semaphore = asyncio.Semaphore(3)  # max 3 workers
    tasks = [asyncio.create_task(worker(i, semaphore)) for i in range(1, 7)]
    await asyncio.gather(*tasks)

asyncio.run(main())