'''
Задача 3: "Очередь на загрузку"
Условие:
Напишите программу, имитирующую загрузчик файлов с ограничением в 2 одновременные загрузки.
Создайте семафор с лимитом 2.
Напишите корутину download(file_id, semaphore), которая захватывает семафор, ждет 0.1 секунды и возвращает строку Файл {file_id} загружен.
В main запустите 5 задач download() для file_id от 0 до 4.
Соберите результаты с помощью asyncio.gather() и напечатайте их.
Входные данные:
Нет.
Выходные данные:
Результаты должны быть в списке в том же порядке, в котором задачи были переданы в gather.
Sample Input:
Sample Output:
['Файл 0 загружен', 'Файл 1 загружен', 'Файл 2 загружен', 'Файл 3 загружен', 'Файл 4 загружен']
'''

import asyncio


async def download(file_id, semaphore):
    async with semaphore:
        await asyncio.sleep(0.1)
        return f'Файл {file_id} загружен.'

async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = [download(i,semaphore) for i in range(5)]
    result = await asyncio.gather(*tasks)
    print(result)

asyncio.run(main())