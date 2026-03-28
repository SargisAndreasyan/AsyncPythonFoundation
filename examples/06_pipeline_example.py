import asyncio
import random

async def generate_data(queue, count):
    for i in range(1, count+1):
        await asyncio.sleep(random.uniform(0, 0.5))
        data = {"id": i, "status": "raw"}
        await queue.put(data)
        print(f"[GENERATOR] {data}")
    await queue.put(None)  # sentinel

async def worker(worker_id, input_queue, output_queue, semaphore):
    while True:
        async with semaphore:
            data = await input_queue.get()
            if data is None:
                await input_queue.put(None)
                break
            await asyncio.sleep(random.uniform(0.1, 1.0))
            data["status"] = "processed"
            print(f"[WORKER {worker_id}] {data}")
            await output_queue.put(data)

async def aggregator(input_queue, count):
    for _ in range(count):
        data = await input_queue.get()
        print(f"[AGGREGATOR] {data}")

async def main():
    raw_queue = asyncio.Queue()
    processed_queue = asyncio.Queue()
    semaphore = asyncio.Semaphore(3)
    count = 10

    workers = [asyncio.create_task(worker(i, raw_queue, processed_queue, semaphore)) for i in range(1, 4)]
    aggregator_task = asyncio.create_task(aggregator(processed_queue, count))

    await generate_data(raw_queue, count)
    await aggregator_task
    await asyncio.gather(*workers)

asyncio.run(main())