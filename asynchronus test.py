import asyncio
import time



def downs():
    x = 100
    while x > 0:
        print(x)
        time.sleep(0.1)
        x -= 1


async def up(num):
    x = num
    while x != 100:
        print(x)
        time.sleep(0.1)
        await asyncio.sleep(1)
        x += 1
        return x
##




async def counting():
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(up,down)]

    await asyncio.gather(*tasks)

##
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def down(start, stop, secs):
    for i in range(start, stop):
        print(i)
        time.sleep(secs)
        await asyncio.sleep(5)
    return i 
        






async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        down(10, 20, 1),
        down(100, 130, 1),
        down(3000, 3050, 1),
        return_exceptions=True
    )
    print(L)

asyncio.run(main(), debug=True)



    
