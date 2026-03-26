import asyncio

balance = 100
lock = asyncio.Lock()


async def withdraw(amount):
    global balance
    async with lock:
        if balance >= amount:
            await asyncio.sleep(0.1)
            balance -= amount
            print('Снятие успешно')
        else:
            print('Недостаточно средств')


async def main():
    await asyncio.gather(withdraw(70),withdraw(70))
    print(balance)

asyncio.run(main())