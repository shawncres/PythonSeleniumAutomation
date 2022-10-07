from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
import time
import unittest
import warnings
import random
import warnings
from Locators_HM import assemblies_locators
from Locators_HM import ri_locators

def setupRI():
    '''Initiates selenium and pulls up the Robot Identification page'''
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

def setRIN():
    '''Asks for RIN to be used in Ant creation throughout the test'''
    global RIN
    RIN = input('What is the Ants friendly name?: ').strip().upper()
    print(RIN)

def getGUID():
    '''Uses preset RIN to extract the GUID to be used in later parenting logic'''
    global GUID
    driver.get(ri_locators.ri_page)
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.searchbox).send_keys(RIN)
    driver.find_element(by = By.XPATH, value=ri_locators.searchBtn).click()
    time.sleep(3)
    GUID = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[3]/table/tbody/tr/td[1]').text  
    print(GUID)
    

def setWO():
    '''Generates s random Work Oder ID to be used for Assemblies and stores it'''
    global randomWOID
    randomWOID = 'WO' + str(random.randrange(100000,999999,1))    
    print(randomWOID)

def assignWO():
    '''Uses the pre-set WO for use in the serialization page'''
    driver.find_element(by=By.XPATH, value=assemblies_locators.WOnumber).send_keys(randomWOID)

def partlist52():
    ''' Ant partlist to be used for 5.2 ants specifically for use in serialization and parenting logic'''
    global partLists
    partLists = [['149269', '142135', '149816', '152881', '152585', '150705', '145135'],
                     ['149278', '146530', '149818'], ['149272', '149818', '146228'],
                     ['149270', '149820', '152395', '152395', '146445', '146445', '145133', '149683'],
                     ['149271', '149820', '152395', '152395', '146445', '146445']]
    partLists.append(partLists[3])
    partLists.append(partLists[4])
    

def serialization():
    '''Serializes all the parts from the provided Partlist and created a nestled serial list for use in parenting'''
    global serialLists
    serialLists = []
    for partList in partLists:
        serialList = []
        for i in partList:
            driver.get(assemblies_locators.assign_page)
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=assemblies_locators.part_number).send_keys(i)
            serialNumber = i + '-' + RIN + '-' + str(random.randrange(1000, 9999, 1))
            driver.find_element(by=By.XPATH, value=assemblies_locators.serial_number).send_keys(serialNumber)
            time.sleep(2)
            assignWO()
            time.sleep(1)
            driver.find_element(by=By.XPATH, value=assemblies_locators.assign_but).click()
            serialList.append(serialNumber)
            time.sleep(2)
        serialLists.append(serialList)
        time.sleep(3)
    print(serialLists)

def serialscount():
    '''Validates the number of parts that were serialized'''
    x = 0
    for i in serialLists:
        x += len(i)
    print(f'{x} parts have been serialized')

def parentingSA():
    '''Assembles all the subassemblies using the serial lists that was previously generated'''
    driver.get(assemblies_locators.parent_page)
    time.sleep(3)
    for serialList in serialLists:
        for i in serialList:
                if serialList[0] != i:
                    try:
                        time.sleep(5)
                        snfield1 = driver.find_element(by=By.XPATH, value=assemblies_locators.sn1_field)
                        snfield1.send_keys(serialList[0])
                        time.sleep(3)
                        snfield2 = driver.find_element(by=By.XPATH, value=assemblies_locators.sn2_field)
                        snfield2.send_keys(i)
                        time.sleep(6)
                        parentButton = driver.find_element(by=By.XPATH, value=assemblies_locators.parentchild_but)
                        parentButton.click()
                        time.sleep(6)
                        driver.get(assemblies_locators.parent_page)
                    except:                        
                        continue
    print(f'{len(serialLists)} subassemblies assembled')



            ## CheckList and Final attaching logic of the Subassembly to the Ant Can this be combined with the above step or should this be completed as a final sequence once
def checklists():
    '''When on a subassembly page or on the Ant page this command completes and saves checklist if applicable'''
    try:        
        cb = driver.find_elements(by=By.CSS_SELECTOR, value='input[type=checkbox]')
        for i in cb:
            i.click()
    except StopIteration:
        pass
    except ElementClickInterceptedException:
        pass    
        time.sleep(3)

    try:
        cbsave = driver.find_element(by=By.CSS_SELECTOR,
                                     value='#application > div.pusher > div > div:nth-child(1) > div > div > div:nth-child(3) > div.ui.bottom.attached.tab.segment.active > div > div > div.six.wide.column > div > button')
        cbsave.click()
        time.sleep(3)        
    except NoSuchElementException:        
        print('QA checklist not required for this Subassembly')
        pass


def commission():
    try:
        cbcomission = driver.find_element(by=By.CSS_SELECTOR,
                                          value='#application > div.pusher > div > div:nth-child(1) > div > div > div.ui.internally.celled.top.aligned.very.compact.grid > div:nth-child(1) > div.eight.wide.right.floated.right.aligned.column > span.ui.fluid > button')
        cbcomission.click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div.ui.internally.celled.top.aligned.very.compact.grid > div:nth-child(1) > div.eight.wide.right.floated.right.aligned.column > a:nth-child(2) > button').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[1]/div/div[1]/div[1]/div[2]/div/button').click()
        time.sleep(2)
    except:
        pass 

def newSAattach():
    driver.get(assemblies_locators.parent_page)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=assemblies_locators.sn1_field).send_keys(GUID)
    x = len(serialLists)
    i = 0
    while x > 0:
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=assemblies_locators.sn2_field).send_keys(serialLists[i][0])
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=assemblies_locators.parentchild_but).click()
        driver.find_element(by=By.XPATH, value=assemblies_locators.sn2_field).clear()    
        i += 1
        x -= 1
    print(f'{len(serialLists)} subassemblies attached')

def newchecklists():
    x = len(serialLists)
    i = 0
    while x > 0:
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#hierarchy".format(serialLists[i][0]))
        time.sleep(3)
        checklists()
        time.sleep(3)
        commission()
        i += 1
        x -= 1
        
def antcommission():
    time.sleep(4)
    driver.get("https://attabotics-hivemind-test.azurewebsites.net/commissioning/ants/{0}#comm".format(GUID))
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button[4]').click()
        time.sleep(5)        
    except NoSuchElementException:
        print('Could not Commission')
        pass
    print('Ant Commissioning Successful')


def assembliescommission():
    for i in serialLists:
        
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/commissioning/assemblies/{0}#comm".format(i[0]))
        time.sleep(3)
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[1]/div/div[1]/div[1]/div[2]/div/button').click()
            time.sleep(3)
        except:
            print(f'{i[0]} subassembly does not need to be comissioned')
        
    print('All remaining subassemblies now in Commission')
        













## Function to send assertations to Pytest, 
def finalization():
    time.sleep(3)
    driver.get(
        "https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#heirarchy".format(GUID))
    time.sleep(3)
    global serialzerovalidation
    serialzerovalidation = driver.find_element(by=By.XPATH,
                                               value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div')
    print(serialzerovalidation.text[:1])
    self.assertEqual(serialzerovalidation.text[:1], '0', 'All Sub-assemblies not attached!')
    print('Ant fully assembled successfully!')
    time.sleep(3)
    driver.close()



if __name__ == '__main__':
    setRIN()
    setupRI()
    getGUID()
    setWO()
    partlist52()
    serialization()
    serialscount()
    parentingSA()
    newchecklists()
    newSAattach()
    antcommission()
    assembliescommission()


    
