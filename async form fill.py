import asyncio
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver= webdriver.Edge()
driver.get('https://phptravels.com/demo/')

firstfield = '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[1]'
lastfield = '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[2]'
bus = '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[3]'
email = '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[4]'
res = '//*[@id="number"]'
def maths():    
    l = driver.find_element(by=By.XPATH, value='//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/h2')
    j = (l.text).split(' ')
    m = [int(i) for i in j if i.isalnum()]
    return sum(m)

collection = {firstfield:'Jack', lastfield:'Dorsey', bus:'twitter', email:'jack@twitter.com', res:maths()}



async def fillfields(b):
    for k,v in b.items():        
        c = driver.find_element(by=By.XPATH, value=k)
        c.send_keys(v)
    await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        fillfields(collection),
        return_exceptions=True)

        
asyncio.run(main(), debug=True)


