import asyncio


# Корутина, которая всегда "ломается"
async def risky_operation():
    print("Начинаю рискованную операцию...")
    await asyncio.sleep(1)
    # Здесь происходит ошибка
    return 10 / 0


async def main():
    print("Попытка выполнить рискованную операцию.")
    try:
        # Оборачиваем await в try...except
        result = await risky_operation()
        print(f"Операция успешна, результат: {result}")
    except ZeroDivisionError:
        print("Поймал ошибку! Деление на ноль внутри корутины.")

    print("Программа продолжает работу.")


asyncio.run(main())