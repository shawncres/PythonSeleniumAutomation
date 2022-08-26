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
from Locators_RI import ri_locators

driver = webdriver.Edge()
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

GUID = ''

class TestAntCreation(unittest.TestCase):
    
    def test_1(self):
        

        driver.get(ri_locators.ri_page)
        randomWOID = 'WO' + str(random.randrange(100000,999999,1))

        time.sleep(3)
        if randomWOID in driver.page_source:
            randomWOID = 'WO' + str(random.randrange(100000,999999,1))
        else:
            randomWOID == randomWOID
            
        driver.find_element(by = By.XPATH, value=ri_locators.create).click()

        driver.find_element(by = By.XPATH, value=ri_locators.generate).click()
        global GUID 
        GUID = driver.find_element(by=By.XPATH, value=ri_locators.GUIDfield).get_attribute('value')
        print(GUID)


        driver.find_element(by=By.CSS_SELECTOR, value=ri_locators.GeneralAssembly).click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=ri_locators.ant5_2).click()

        driver.find_element(by = By.XPATH, value=ri_locators.RINgenerate).click()

        print(randomWOID)
        driver.find_element(by=By.XPATH, value=ri_locators.WOnumberfld).send_keys(randomWOID)


        randomRadioID = str(random.randrange(1000,9999,1))+ ':'+ str(random.randrange(1000,9999,1)) + random.choice(['a','b','v','x'])+ str(random.randrange(111,999,1)) 
        driver.find_element(by=By.XPATH, value=ri_locators.radioID).send_keys(randomRadioID)

        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.saveRI).click()

        time.sleep(3)

        if GUID in driver.page_source:
            print('Robot Identity successfully created')    
        else:
            print('Creation of Robot Failed')
            
        self.assertTrue(GUID in driver.page_source)    
            
        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.searchbox).send_keys(GUID)
        driver.find_element(by = By.XPATH, value=ri_locators.searchBtn).click()
        time.sleep(3)
        driver.find_element(by = By.XPATH, value=ri_locators.viewassemblyBtn).click()
        ##driver.close()

        time.sleep(3)
        RINfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]')
        RIN = RINfield.text

        print(RIN)
        driver.close()

    def assembly_2(self):
        '''Takes Global GUID from prior test, serializes and assembles all subassemblies.'''
        partLists=[['149269', '142135', '149816', '152881', '152585', '150705', '145135'], ['149278', '146530', '149818'], ['149272', '149818', '146228'], ['149270', '149820', '152395', '152395', '146445', '146445', '145133', '149683'], ['149271', '149820', '152395', '152395', '146445', '146445']]
        partLists.append(partLists[3])
        partLists.append(partLists[4])

        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#heirarchy".format(GUID))
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(3)
        RINfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[1]/div/div[1]')
        RIN = RINfield.text

        print(RIN)


        for partList in partLists:
            serialList=[]

            ## Serial assignation to all specific parts from part list, possible iteration logic needs to be done to go over each sub assembly part 

            for i in partList:
                driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/assign_serial_number")

                time.sleep(5)
                pnfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input')
                pnfield.send_keys(i)


                snfield = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input')
                serialNumber = i+'-'+RIN+'-'+str(random.randrange(1000,9999,1))                
                snfield.send_keys(serialNumber)
                time.sleep(3)
                assignButton = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/button')
                assignButton.click()
                serialList.append(serialNumber)
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
                    try:                        
                        time.sleep(5)
                        snfield1 = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input')
                        snfield1.send_keys(serialList[0])
                        time.sleep(3)
                        snfield2 = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input')
                        snfield2.send_keys(i)
                        time.sleep(6)
                        parentButton = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[2]/div/button')
                        parentButton.click()
                        time.sleep(6)
                        driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/parent_serial_number")
                    except:
                        continue


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
                time.sleep(3)
                cbcomission= driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div.ui.internally.celled.top.aligned.very.compact.grid > div:nth-child(1) > div.eight.wide.right.floated.right.aligned.column > span.ui.fluid > button')
                cbcomission.click()
                time.sleep(3)
                driver.switch_to.alert.accept()
            except NoSuchElementException:
                print('QA checklist not required for this Subassembly')
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
            

        time.sleep(4)
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/commissioning/ants/{0}#comm".format(GUID))
        time.sleep(3)
        markInComission = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button[4]')
        markInComission.click()            
        time.sleep(3)
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#heirarchy".format(GUID))
        time.sleep(3)
        serialzerovalidation = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div')
        print(serialzerovalidation.text[:1])
        self.assertEqual(serialzerovalidation.text[:1],'0','All Sub-assemblies not attached!')
        print('Ant fully assembled successfully!')







if __name__ == '__main__':
    unittest.main()
