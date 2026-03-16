import asyncio

async def prepare():
    await asyncio.sleep(1)
    print("prepare")

async def execute():
    await asyncio.sleep(2)
    print("execute")

async def cleanup():
    await asyncio.sleep(3)
    print("cleanup")

async def main():
    await prepare()
    await execute()
    await cleanup()



asyncio.run(main())