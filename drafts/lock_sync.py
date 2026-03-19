import asyncio

# Наш общий ресурс, который будут изменять все задачи
COUNTER = 0
# Сколько задач мы хотим запустить
TASKS_COUNT = 10_000

# Lock создается один раз вне корутин
lock = asyncio.Lock()


async def increment():
    global COUNTER

    # Теперь вся опасная работа происходит внутри "async with"
    async with lock:
        # --- НАЧАЛО КРИТИЧЕСКОЙ СЕКЦИИ ---
        # Только одна задача может быть здесь в один момент времени!
        temp_counter = COUNTER
        await asyncio.sleep(0)
        COUNTER = temp_counter + 1
        # --- КОНЕЦ КРИТИЧЕСКОЙ СЕКЦИИ ---

async def main():
    print(f"Ожидаемое значение счетчика: {TASKS_COUNT}")

    # Запускаем 10 000 задач конкурентно
    tasks = [increment() for _ in range(TASKS_COUNT)]
    await asyncio.gather(*tasks)

    print(f"Итоговое значение счетчика: {COUNTER}")


# Запускаем программу
asyncio.run(main())