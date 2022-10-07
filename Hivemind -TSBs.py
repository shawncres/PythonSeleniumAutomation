from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.options import Options
import time
import unittest
import selenium
import random
import warnings
from Locators_HM import tsb_locators



def setupTSB():        
        global driver
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.get(tsb_locators.tsb_page)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        global tsbList
        tsbList = []


def createTSB():        
        time.sleep(5)
        driver.find_element(by=By.XPATH, value=tsb_locators.create).click()



def nameID(e):
        global idname
        idname= e+' Test-TSB-'+str(random.randrange(1000,9999,1)) 
        time.sleep(4)
        print(idname)
        tsbList.append(idname)
        driver.find_element(by=By.XPATH, value=tsb_locators.id_box).send_keys(idname)
        

def detailsTSB():
        '''The Link to Document, random Priority and Optional/Mandatory selection'''
        time.sleep(2)                
        driver.find_element(by=By.XPATH, value=tsb_locators.link_box).send_keys('https://attabotics.sharepoint.com/:u:/s/SoftwareQATeam/ETMkBqusyUBMswCwrgOLRugBCm8UaR8wn51iP3G2GyeEYA?e=eHETYk')
        
        randomPriorityvalue='/html/body/div[2]/div/div[2]/div/form/div[2]/div[3]/div/div[{0}]/div/input'.format(str(random.randrange(1,4,1)))
        priority=driver.find_element(by=By.XPATH, value=randomPriorityvalue)
        priority.click()

        randomMandatoryValue='/html/body/div[2]/div/div[2]/div/form/div[2]/div[4]/div/div[{0}]/div/input'.format(str(random.randrange(1,3,1)))
        Mandatory=driver.find_element(by=By.XPATH, value=randomMandatoryValue)
        Mandatory.click()  


def entitySelect(ent):
        time.sleep(2)                
        entityType=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[2]/div[1]/div/input')
        entityType.click()

        time.sleep(3)

        entity= f'/html/body/div[2]/div/div[2]/div/form/div[2]/div[1]/div/div/div[{str(ent)}]'
        global entname
        entname = driver.find_element(by=By.XPATH, value=entity).text
        driver.find_element(by=By.XPATH, value=entity).click()


##dueDate=driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div[2]/div/span[33]')
##dueDate.send_keys('2022-04-21 12:00')
##dueDate.click()
def dateSelect():
                
        cal=driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[2]/div[2]/input[2]')
        cal.click()
        time.sleep(3)
        today=driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div[2]/div/span[35]')
        today.click()

  
def selectEntities():
        try:
                driver.find_element(by=By.CSS_SELECTOR, value=tsb_locators.first_option).click()    
                time.sleep(3)
        except:
                pass
        
        driver.find_element(by=By.XPATH, value=tsb_locators.save_tsb).click()


def validation():
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=tsb_locators.search).send_keys(idname)
        time.sleep(6)
        if idname in driver.page_source:
                print('TSB created successfully')
        else:
                print('TSB not found')
        driver.find_element(by=By.XPATH, value=tsb_locators.search).clear()



## Drop  down box problems to complete list, don't forget to delete the hardcoded list for the rest of the test to work after this is fixed,
## possible fix is the select module of selenium to select things in drop down boxes better         
def completingTSBs():
        tsbList = ['Ant Test-TSB-3736', 'Work Station Test-TSB-6813', 'Ant Hill Test-TSB-3539', 'Cap Bank Test-TSB-6392', 'Site Test-TSB-6731', 'Structure Test-TSB-4216', 'System Panel Test-TSB-2505', 'Radio Panel Test-TSB-7492', 'Sub Assembly Instance Test-TSB-4343']
        for i in tsbList:
                driver.get(tsb_locators.tsb_page)
                time.sleep(10)
                driver.find_element(by=By.XPATH, value=tsb_locators.search).send_keys(i)
                time.sleep(6)
                driver.find_element(by=By.XPATH, value=tsb_locators.details).click()
                time.sleep(3)
                driver.find_element(by=By.XPATH, value=tsb_locators.details_tsb).click()
                time.sleep(3)
                driver.find_element(by=By.XPATH, value=tsb_locators.update_tsb).click()
                time.sleep(3)
                driver.find_element(by=By.CSS_SELECTOR, value=tsb_locators.status_tsb).click()
                time.sleep(3)
                driver.find_element(by=By.XPATH, value=tsb_locators.complete_tsb).click()
                time.sleep(3)
                driver.find_element(by=By.XPATH, value=tsb_locators.save_status).click()                
                
                
                
        pass



def main():
        setupTSB()
        ent = 1
        while ent <10:
                createTSB()                
                detailsTSB()
                entitySelect(ent)
                nameID(entname)
                dateSelect()
                selectEntities()
                validation()
                ent+=1
        print(tsbList)
        driver.close()


if __name__ == '__main__':
        setupTSB()
        completingTSBs()







##sortDate=driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[2]/div[3]/div/table/thead/tr/th[5]/a/span')
##sortDate.click()
##time.sleep(4)






##
##Assertion
##time.sleep(15)
##self.assertTrue(idname in driver.page_source)







