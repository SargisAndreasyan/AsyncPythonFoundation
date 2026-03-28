import asyncio
import random

async def generate_data(output_queue: asyncio.Queue, items_count):
    for i in range(1, items_count + 1):
        await asyncio.sleep(random.uniform(0, 0.5))
        data = {"id": i, "status": "raw"}
        print(f"[ГЕНЕРАТОР] Сгенерированы данные: {data}")
        await output_queue.put(data)


async def process_data(worker_id, input_queue, output_queue, semaphore):
    try:
        while True:
            async with semaphore:
                data = await input_queue.get()
                if data is None:
                    await input_queue.put(None)
                    print(f"[ВОРКЕР {worker_id}] завершён")
                    break

                await asyncio.sleep(random.uniform(0.1, 1.0))
                data["status"] = "processed"
                print(f"[ВОРКЕР {worker_id}] Обработаны данные: {data}")
                await output_queue.put(data)

    except asyncio.CancelledError:
        print(f"[ВОРКЕР {worker_id}] отменён")
        raise


async def aggregate_results(input_queue, items_count):
    for _ in range(items_count):
        data = await input_queue.get()
        print(f"[АГРЕГАТОР] Получен результат: {data}")


async def main():
    raw_queue = asyncio.Queue()
    processed_queue = asyncio.Queue()
    semaphore = asyncio.Semaphore(3)
    items_count = 10
    workers_count = 3

    workers = [
        asyncio.create_task(process_data(i, raw_queue, processed_queue, semaphore))
        for i in range(1, workers_count + 1)
    ]
    aggregator = asyncio.create_task(aggregate_results(processed_queue, items_count))
    await generate_data(raw_queue, items_count)
    await raw_queue.put(None)
    await aggregator
    await asyncio.gather(*workers)

asyncio.run(main())