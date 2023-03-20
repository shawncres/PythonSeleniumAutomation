import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import uuid
import random
from webdrivermanager import *

## Issue Search

def setup():
    global driver
    driver = startEdgeDriver()
    driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/ants/176a8ec3-2ad5-aaab-d9b5-7db45eaf45b0#comm')



def function1(x,y):
    time.sleep(x)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[3]/div[2]/div[5]/div[2]/table/tfoot/tr/td/div/div/input').click()
    time.sleep(x)
    ## Creates and prints variables for all 3 issue fields
    global issueType
    issueType = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[3]/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[2]').text
    global issueRes
    issueRes = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[3]/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[4]').text
    global issueNote
    issueNote = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[3]/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[6]').text
    print(issueType)
    print(issueRes)
    print(issueNote)
    ## Navigate to Issue serach page and search for above fields
    driver.get('https://attabotics-hivemind-test.azurewebsites.net/commissioning/issues')
    time.sleep(y)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[1]/input').send_keys(issueType.split()[1].strip('()'))
    time.sleep(x)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[3]/button').click()
    time.sleep(x)
    if issueType in driver.page_source:
        print('Issue Type was found')
    else:
        print('Issue Type was not found')

def function2():    
    time.sleep(5)   
    ## Switches to resolution and clear the existing field before searching for the resolution
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[2]/div[1]/input').click()
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[2]/div[2]/input').click()
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[1]/input').clear()
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[1]/input').send_keys(issueRes)
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[3]/button').click()
    time.sleep(2)
    if issueRes in driver.page_source:
        print('Issue Resolution was found')
    else:
        print('Issue Resolution was not found')

def function3():    
    time.sleep(5)
    ## Switches to notes and clear the existing field before searching for the note
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[2]/div[2]/input').click()
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[2]/div[3]/input').click()
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[1]/input').clear()
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[1]/input').send_keys(issueNote)
    time.sleep(2)
    driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/form/div/div[3]/button').click()
    time.sleep(2)
    if issueNote in driver.page_source:
        print('Issue Note was found')
    else:
        print('Issue Note was not found')
    time.sleep(5)

def teardown():    
    driver.close()

if __name__ == '__main__':
    setup()
    function1(5,8)
    function2()
    function3()
    teardown()
