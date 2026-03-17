import asyncio


async def get_user(user_id):
    print(f"Скачиваю пользователя {user_id}...")
    await asyncio.sleep(1)
    return f"User({user_id})"


async def get_transactions(user_id):
    print(f"Скачиваю транзакции {user_id}...")
    await asyncio.sleep(2)
    return ["Tx1", "Tx2", "Tx3"]


async def main():
    print("--- Начало работы TaskGroup ---")

    # Создаем группу задач.
    # Python гарантирует: мы не пойдем дальше этого блока, пока все задачи не решатся.
    async with asyncio.TaskGroup() as tg:
        # Запускаем задачи и сохраняем ССЫЛКИ на них (task objects)
        task_user = tg.create_task(get_user(42))
        task_trans = tg.create_task(get_transactions(42))

        print("Задачи запланированы, ждем завершения блока...")

    # --- Точка синхронизации ---
    # Если мы попали сюда, значит ВСЕ задачи внутри tg успешно завершились.
    # Теперь можно безопасно доставать результаты.

    print(f"Пользователь: {task_user.result()}")
    print(f"Транзакции:   {task_trans.result()}")
    print("--- Конец ---")


if __name__ == "__main__":
    asyncio.run(main())