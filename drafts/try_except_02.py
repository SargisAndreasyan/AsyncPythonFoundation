import asyncio


async def get_user_data(user_id):
    """
    Имитирует запрос данных пользователя.
    Падает с ошибкой, если user_id равен 0.
    """
    print(f"Запрашиваю данные для пользователя {user_id}...")
    await asyncio.sleep(1)  # Имитация сетевой задержки

    if user_id == 0:
        # Генерируем исключение, как будто пользователя не нашли
        raise ValueError(f"Пользователь с ID {user_id} не найден!")

    # Этот код не выполнится для user_id=0
    return {"id": user_id, "name": "Alice"}


async def main():
    print("--- Попытка 1: Запрашиваем существующего пользователя (ID=1) ---")
    try:
        user = await get_user_data(1)
        print(f"Успех! Данные получены: {user}")
    except ValueError as e:
        print(f"Произошла ошибка: {e}")

    print("\n" + "=" * 40 + "\n")

    print("--- Попытка 2: Запрашиваем несуществующего пользователя (ID=0) ---")
    try:
        user = await get_user_data(0)
        # Эта строка никогда не будет выполнена
        print(f"Успех! Данные получены: {user}")
    except ValueError as e:
        # Исключение, возникшее в get_user_data, будет поймано здесь
        print(f"Произошла ошибка, как и ожидалось: {e}")

    print("\nПрограмма корректно завершила работу.")


# Запускаем программу
asyncio.run(main())