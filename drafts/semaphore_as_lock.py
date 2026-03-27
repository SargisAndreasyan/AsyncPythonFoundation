"""
Задача 2: "Семафор как замок"
Условие:
Докажите, что asyncio.Semaphore(1) ведет себя точно так же, как asyncio.Lock().
Напишите программу с двумя корутинами:

task_a(semaphore): Захватывает семафор, печатает "A start", ждет 0.1 сек, печатает "A end".

task_b(semaphore): Захватывает семафор, печатает "B start", ждет 0.1 сек, печатает "B end".

В main создайте asyncio.Semaphore(1) и запустите обе задачи конкурентно, передав им этот семафор.

Входные данные:
Нет.

Выходные данные:
Вывод должен быть строго последовательным, доказывая, что вторая задача ждала первую.

Sample Input:

Sample Output:

A start
A end
B start
B end

"""

import asyncio

async def task_a(semaphore):
    async with semaphore:
        print("A start")
        await asyncio.sleep(0.1)
        print("A end")

async def task_b(semaphore):
    async with semaphore:
        print("B start")
        await asyncio.sleep(0.1)
        print("B end")

async def main():
    semaphore = asyncio.Semaphore(1)
    tasks = [task_a(semaphore), task_b(semaphore)]
    await asyncio.gather(*tasks)

asyncio.run(main())