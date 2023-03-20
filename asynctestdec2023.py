import asyncio
import random


async def randoms(x):
    return random.randint(1,x)

async def main():    
    f = await asyncio.gather(
        randoms(19),
        randoms(566),
        randoms(343434)
        )
    print(f)

asyncio.run(main())



    



