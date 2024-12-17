import asyncio


async def start_strongman(name: str, power: int) -> None:
    print(f"Силач {name} начал соревнования")
    for attempt in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {attempt}")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament() -> None:
    task_pasha = asyncio.create_task(start_strongman("Pasha", 3))
    task_denis = asyncio.create_task(start_strongman("Denis", 4))
    task_apolon = asyncio.create_task(start_strongman("Apollon", 5))
    await task_pasha
    await task_denis
    await task_apolon


asyncio.run(start_tournament())
