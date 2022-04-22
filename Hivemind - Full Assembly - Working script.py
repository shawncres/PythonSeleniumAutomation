from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import selenium
import random


GUID=input('Enter Ant UID:')


## Manual part list provided need to Automatically create a dictionary from scraping the parts table
## Will need to utilize a method that understands the Subassembly number vs Part number for parenting purposes later
partLists=[['149269','150710','149816','152881','152585','150705','145135'],['149278','146530','149818'],['149272','149818','146228'],['149270','149820','152395','152395','146445','146445','145133','149683',],['149271','149820','152395','152395','146445','146445']]
partLists.append(partLists[3])
partLists.append(partLists[4])

driver = webdriver.Edge()
driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#heirarchy".format(GUID))

time.sleep(3)
RINfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]')
RIN = RINfield.text

print(RIN)


for partList in partLists:
    serialList=[]

    ## Serial assignation to all specific parts from part list, possible iteration logic needs to be done to go over each sub assembly part 

    for i in partList:
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/assign_serial_number")

        time.sleep(3)
        pnfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input')
        pnfield.send_keys(i)


        snfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input')
        serialNumber = i+'-'+RIN+'-'+str(random.randrange(1000,9999,1))
        serialList.append(serialNumber)
        snfield.send_keys(serialNumber)


        time.sleep(3)
        assignButton = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/button')
        assignButton.click()
        time.sleep(2)

    time.sleep(3)
    driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/parent_serial_number")
    time.sleep(3)

    print(serialList)

    ## Parenting logic to attach each component to its parent subassembly, utilizing the serial list created in above logic,
    ## Important to not the Subassembbly is diffrentiated only by it's position as first element on the list, hence serial lists need to be kept separate
    ## Need to find a way to capture/process lists separately or to indicate the position of the subassembly vs part in a singular list, possibly a panda's grid, so far colour is the indicator

    for i in serialList:
        if serialList[0] != i:
            time.sleep(2)
            snfield1 = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input')
            snfield1.send_keys(serialList[0])
            time.sleep(3)
            snfield2 = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input')
            snfield2.send_keys(i)
            time.sleep(4)
            parentButton = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[2]/div/button')
            parentButton.click()
            time.sleep(5)
            driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/parent_serial_number")



    ## CheckList and Final attaching logic of the Subassembly to the Ant Can this be combined with the above step or should this be completed as a final sequence once 
    time.sleep(4)
    driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#hierarchy".format(serialList[0]))
            
    time.sleep(3)

    try:
        cb = driver.find_elements(by=By.CSS_SELECTOR, value='input[type=checkbox]')
        for i in cb:
            i.click()
    except StopIteration:
        pass

    time.sleep(3)

    try:
        cbsave= driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div:nth-child(3) > div.ui.bottom.attached.tab.segment.active > div > div > div.six.wide.column > div > button')
        cbsave.click()
    except NoSuchElementException:
        print('element not found')
        pass

    time.sleep(3)
    assignParentButt=driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div.ui.internally.celled.top.aligned.very.compact.grid > div:nth-child(1) > div.eight.wide.right.floated.right.aligned.column > a > button')
    assignParentButt.click()


    time.sleep(5)
    snfield2 = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input')
    snfield2.send_keys(GUID)
    time.sleep(3)
    parentButton = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[2]/div/button')
    parentButton.click()
    serialList=[]
    print(serialList)

    
time.sleep(3)
driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#heirarchy".format(GUID))
print('All Ant sub-assemblies completed')






