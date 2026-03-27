'''
Задача 5: "Подготовка и работа"
Условие:
Напишите программу, которая докажет, что семафор ограничивает только определенную часть работы.
Создайте корутину worker(worker_id, semaphore).
Внутри нее должны быть две фазы: "Подготовка" (имитируется через await asyncio.sleep(0.1)) и "Работа" (имитируется через await asyncio.sleep(0.2)).
Только фаза "Работы" должна быть защищена семафором с лимитом 2.
Вам нужно подсчитать, сколько воркеров одновременно находилось в фазе "Подготовки", и сколько — в фазе "Работы".
Для этого:
Создайте глобальные счетчики и переменные для максимумов: preparing_count, max_preparing, working_count, max_working.
Используйте asyncio.Lock для безопасного изменения этих счетчиков.
Внутри worker увеличивайте/уменьшайте соответствующие счетчики до и после каждой фазы.
В main запустите 4 воркера.
После их завершения, выведите два числа на отдельных строках: сначала max_preparing, затем max_working.
Входные данные:
Нет.
Выходные данные:
Программа должна показать, что в фазе подготовки могли находиться все 4 воркера, а в фазе работы — не более 2.
'''
import asyncio

semaphore = asyncio.Semaphore(2)

MAX_PREPARE_COUNT = 0
MAX_WORKING_COUNT = 0
WORKERS = []
PREPARE_WORKERS = []

async def worker(worker_id, semaphore):
    # Prepare
    global MAX_PREPARE_COUNT, MAX_WORKING_COUNT, WORKERS, PREPARE_WORKERS
    PREPARE_WORKERS.append(worker_id)
    await asyncio.sleep(0.1)
    MAX_PREPARE_COUNT = max(MAX_PREPARE_COUNT, len(PREPARE_WORKERS))
    async with semaphore:
        WORKERS.append(worker_id)
        MAX_WORKING_COUNT = max(MAX_WORKING_COUNT, len(WORKERS))
        await asyncio.sleep(0.2)
        WORKERS.remove(worker_id)

async def main():
    tasks = [worker(i,semaphore) for i in range(4)]
    await asyncio.gather(*tasks)
    print(MAX_PREPARE_COUNT, MAX_WORKING_COUNT)

asyncio.run(main())