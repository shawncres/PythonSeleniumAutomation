from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import unittest
import warnings
import random
import warnings
import qrcode
from Locators_HM import ri_locators


def setupRI():
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    global GUID
    GUID = ''
    driver.get(ri_locators.ri_page)

def checkWO():
    global randomWOID
    randomWOID = 'WO' + str(random.randrange(100000,999999,1))
    if randomWOID in driver.page_source:
        randomWOID = 'WO' + str(random.randrange(100000,999999,1))
    else:
        randomWOID == randomWOID
    print(randomWOID)

def woQR():
    global randomWOID
    qrcode.run_example(data=randomWOID)

def createRI():
    driver.find_element(by = By.XPATH, value=ri_locators.create).click()
    

def generateGUID():    
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.generate).click()
    global GUID 
    GUID = driver.find_element(by=By.XPATH, value=ri_locators.GUIDfield).get_attribute('value')
    print(GUID) 


def v52gen_assembly():
    driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value=ri_locators.ant5_2).click()
    driver.find_element(by = By.XPATH, value=ri_locators.RINgenerate).click()

def v51gen_assembly():
    driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value=ri_locators.ant5_1).click()
    driver.find_element(by = By.XPATH, value=ri_locators.RINgenerate).click()

def v43gen_assembly():
    driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value=ri_locators.ant4_3).click()

def v4namegen():
    time.sleep(3)
    randomantname = random.choice(['a', 'b', 'v', 'x']).upper() + random.choice(['a', 'b', 'v', 'x']).upper() + str(random.randrange(10, 99, 1)) + str('5V4')
    driver.find_element(by=By.XPATH, value=ri_locators.v4namefield).send_keys(randomantname)
    
def WO_entry():
    print(randomWOID)
    driver.find_element(by=By.XPATH, value=ri_locators.WOnumberfld).send_keys(randomWOID)

def radiofield_900():
    randomRadioID = str(random.randrange(1000,9999,1))+ ':'+ str(random.randrange(1000,9999,1)) + random.choice(['a','b','v','x'])+ str(random.randrange(111,999,1)) 
    driver.find_element(by=By.XPATH, value=ri_locators.radioID).send_keys(randomRadioID)

def save_ri():
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.saveRI).click()
    time.sleep(3)
    if GUID in driver.page_source:
        print('Robot Identity successfully created')    
    else:
        print('Creation of Robot Failed')

def checkRIN():
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.searchbox).send_keys(GUID)
    driver.find_element(by = By.XPATH, value=ri_locators.searchBtn).click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.viewassemblyBtn).click()
    time.sleep(3)
    RINfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]')
    global RIN
    RIN = RINfield.text
    print(RIN)
    time.sleep(2)
    driver.close()



##should this include a check on the list page or can this be run prior to a Ant creation to confirm the non reuse of existing WO or split into 2 methods 
def checkWOconflict():
    '''needs to be completed'''
    driver.get(ri_locators.ri_page)
    wo = input('Please enter WO to check: ')
    def check(wo):
        if len(wo.upper()) == 8:
            pass
        elif len(wo.upper()) >= 9:
            print('Too many Charectars for WO')
        else:
            wo = 'WO'+wo
        
    if wo.upper() in driver.page_source:
        print('Succussful check Already used WO not usable')
    else:
        print('Previously unused WO is usable')


if __name__ == '__main__':
    setupRI()
    checkWO()
##    woQR()
    createRI()
    generateGUID()
    v52gen_assembly()
    WO_entry()
    radiofield_900()
    save_ri()    
    checkRIN()
