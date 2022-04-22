from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.options import Options
import time
import unittest
import selenium
import random

options = Options()
options.add_argument("headless")

driver = webdriver.Edge()
driver.get("https://attabotics-hivemind-test.azurewebsites.net/commissioning/bulletins")

time.sleep(15)
createTSBbutton=driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[1]/div[1]/div[2]/button')
createTSBbutton.click()


idname='Test--TSBs-'+str(random.randrange(100,999,1)) 

time.sleep(8)
idBox=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[1]/div[1]/input')
idBox.send_keys(idname)

linkBox=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[1]/div[2]/input')
linkBox.send_keys('https://attabotics.sharepoint.com/:u:/s/SoftwareQATeam/ETMkBqusyUBMswCwrgOLRugBCm8UaR8wn51iP3G2GyeEYA?e=eHETYk')                


entityType=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[2]/div[1]/div/input')
entityType.click()

time.sleep(3)
capbank=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[2]/div[1]/div/div[2]/div[4]')
capbank.click()




##dueDate=driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div[2]/div/span[33]')
##dueDate.send_keys('2022-04-21 12:00')
##dueDate.click()

cal=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[2]/div[2]/input[2]')
cal.click()
time.sleep(3)
today=driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div[2]/div/span[35]')
today.click()

randomPriorityvalue='/html/body/div[2]/div/div[2]/div/form/div[2]/div[3]/div/div[{0}]/div/input'.format(str(random.randrange(1,3,1)))

priorityMed=driver.find_element(by=By.XPATH, value=randomPriorityvalue)
priorityMed.click()
                
saveTSB=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[3]/button[2]')
saveTSB.click()


time.sleep(15)

if idname in driver.page_source:
    print('TSB created successfully')
else:
    print('TSB not found')
##
##
##sortDate=driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[2]/div[3]/div/table/thead/tr/th[5]/a/span')
##sortDate.click()
##time.sleep(4)


