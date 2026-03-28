import asyncio

async def long_task():
    try:
        print("Task started")
        await asyncio.sleep(10)
        print("Task finished")
    except asyncio.CancelledError:
        print("Task was cancelled")

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(1)
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)

asyncio.run(main())