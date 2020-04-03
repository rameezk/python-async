import asyncio
from time import sleep, perf_counter


async def count():
    await asyncio.sleep(1)
    print(1)
    await asyncio.sleep(2)
    print(2)
    await asyncio.sleep(3)
    print(3)


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    t1 = perf_counter()
    asyncio.run(main())
    t2 = perf_counter()
    print(f"Took {(t2 - t1):.2f} seconds")
