import asyncio


async def time_iterator():
    for i in range(1, 10):
        print(i)
        await asyncio.sleep(1)


async def request():
    await asyncio.sleep(4)
    print('Request finished')


async def main():
    task1 = asyncio.create_task(time_iterator())
    task2 = asyncio.create_task(request())

    await task1
    await task2

asyncio.run(main())
