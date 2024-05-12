import asyncio

async def fetch_data():  # async def return coroutine object
    print('Staring fetching data...')
    await asyncio.sleep(2)
    print("Done fetching data...")
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


# task1 = asyncio.create_task => task1 run background
# must have this line: await task1 => trigger run background
# when task1 run background, task2 running
# after task1 finish, task1 goes to main flow and postpone task2 (if this task is still running)
# we need add line: await task2 to get task2 finished if it has postponed
# if we add line: await task2 at the beginning => run all flow above

# async def main():
#     task1 = asyncio.create_task(fetch_data())
#     task2 = asyncio.create_task(print_numbers())
#     # await task1  # try to comment this line
#     value = await task1
#     print(value)
#     await task2  # try comment this line


async def main():
    # await fetch_data()  # if we do not use asyncio.create_task => need to wait finish task to process another task
    task2 = asyncio.create_task(print_numbers())
    await fetch_data()  # try to comment this line
    await task2


asyncio.run(main())
