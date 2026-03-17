import asyncio
import time

async def make_dish(name, cook_time):
    """Корутина, имитирующая приготовление блюда."""
    print(f"Начинаем готовить '{name}' (время: {cook_time} сек)...")
    await asyncio.sleep(cook_time)
    print(f"Блюдо '{name}' готово!")

async def main():
    print("Шеф-повар начинает одновременную готовку.")
    start_time = time.time()

    # Собираем все корутины и запускаем их конкурентно с помощью gather
    await asyncio.gather(
        make_dish("Паста", 3),
        make_dish("Салат", 1),
        make_dish("Хлебная корзина", 0.5)
    )

    end_time = time.time()
    print(f"\nВсе блюда готовы! Общее время: {end_time - start_time:.2f} секунд.")

# Запускаем программу
asyncio.run(main())