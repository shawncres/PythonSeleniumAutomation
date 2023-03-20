import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import uuid
import random
from webdrivermanager import *
from selenium.webdriver.common.keys import Keys

## Issue Search

def setup():
    global driver
    driver = startEdgeDriver()

def issueList():
    time.sleep(2)
    driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/ants/2ae1715f-9d7f-2e6f-709e-acd5a6941a6d#comm')
    time.sleep(8)
    global fieldName
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[3]/div[2]/div[5]/button').click()
    time.sleep(1)
    benny=1
    issues=[]
    while True:
        try:            
            tx=driver.find_element(by = By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div.ui.modal.front.transition.visible.active > div.content > form > div:nth-child(1) > div > div > div:nth-child({0})'.format(benny)).text            
        except:
            break                                   
        issues.append(tx)
        benny+=1
        
    print(issues)
    print(len(issues))
    print(benny)

if __name__ == '__main__':
    setup()
    issueList()
