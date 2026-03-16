import asyncio


async def print_message():
    await asyncio.sleep(0.1)
    print("Задача выполнена!")


async def main():
    asyncio.create_task(print_message())
    print("Главная функция завершена.")


asyncio.run(main())
