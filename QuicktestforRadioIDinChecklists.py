from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time




driver = webdriver.Edge()
driver.implicitly_wait(10)

count = 0

matches = 0
entity = 'Robot' 
term = input('What is the term we are looking for?').strip(' ')
driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/qualitychecklistdefinitions')
i = 1

while True:
    time.sleep(4)
    entityCheck = f'//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[2]/div'
    robot = driver.find_element(by=By.XPATH, value=entityCheck).text
    if robot == entity:
        details = f'//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[1]/a/i'
        driver.find_element(by=By.XPATH, value=details).click()                
        time.sleep(5)
        if term in driver.page_source:
            print(f'We have a match #{i} on list of {entity}')
            matches += 1
        else:
            print('not found')
        driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/qualitychecklistdefinitions')
    else:
        pass
    i += 1

    



print(f'After checking {count} lists, we have {matches} matches for {term}')


##//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[4]/td[2]/div
        

##//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[32]/td[1]/a/i

