'''
Задача 1: "Счетчик активных задач"
Условие:
Напишите программу, которая докажет, что семафор действительно ограничивает количество активных задач.

Создайте глобальные переменные active_tasks = 0 и max_active_tasks = 0.

Создайте семафор с лимитом 3.

Напишите корутину worker(), которая:

Захватывает семафор.

Увеличивает active_tasks, обновляет max_active_tasks, если текущее значение больше.

Ждет 0.1 секунды.

Уменьшает active_tasks.

В main запустите 10 задач worker() конкурентно.

После их завершения напечатайте итоговое значение max_active_tasks.
'''
import asyncio

active_tasks = 0
max_active_tasks = 0
semaphore = asyncio.Semaphore(3)

async def worker():
    global active_tasks, max_active_tasks
    async with semaphore:
        active_tasks += 1
        if max_active_tasks < active_tasks:
            max_active_tasks = active_tasks
            await asyncio.sleep(0.1)
        active_tasks -= 1

async def main():
    await asyncio.gather(*(worker() for _ in range(10)))
    print(max_active_tasks)

asyncio.run(main())