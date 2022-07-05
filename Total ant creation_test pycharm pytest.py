from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import warnings
import random
import warnings

driver = webdriver.Edge()
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

GUID = ''

class TestAntCreation(unittest.TestCase):

    def test_create(self):
            driver.get("https://attabotics-hivemind-test.azurewebsites.net/")
            time.sleep(5)    
        
            ham = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button')
            ham.click()

            time.sleep(2)

            comAnts = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[1]/div[3]/div[2]/a[3]')
            comAnts.click()

            time.sleep(3)
            createAnt = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[1]/div[1]/div/button')
            createAnt.click()


            time.sleep(3)
            guidAnt = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[1]/div/button')
            guidAnt.click()

            time.sleep(3)

            hwvers = driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.scrolling.content > div > form > div:nth-child(2) > div > i')
            hwvers.click()

            time.sleep(3)
            hwvers51 = driver.find_element(by=By.CSS_SELECTOR, value='body > div.ui.dimmer.modals.page.transition.visible.active > div > div.scrolling.content > div > form > div:nth-child(2) > div > div > div:nth-child(8)')
            hwvers51.click()

            RINgen = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[3]/div/button')
            RINgen.click()

            GUIDfield = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[1]/div/input')
            global GUID 
            GUID = GUIDfield.get_attribute('value')
            print(GUID)

            ## 0008:4186a798
            radioID = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[4]/div[1]/input')
            randomRadioID = str(random.randrange(1000,9999,1))+ ':'+ str(random.randrange(1000,9999,1)) + random.choice(['a','b','v','x'])+ str(random.randrange(111,999,1)) 
            radioID.send_keys(randomRadioID)

            time.sleep(5)
            saveAnt = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[3]/button[2]')
            saveAnt.click()
            

            time.sleep(4)
            antassemblypage= 'https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/'+GUID+'#heirarchy'

            driver.get('{0}'.format(antassemblypage))

                
            time.sleep(6)
                        
            if GUID in driver.page_source:
                print('Ant created successfully GUID is {0}'.format(GUID))
            else:
                print('Ant not found')
            self.assertTrue(GUID in driver.page_source)

            driver.close()


class TestAntAssembly(unittest.TestCase):

    def test_create(self):

        ## Manual part list provided need to Automatically create a dictionary from scraping the parts table
        ## Will need to utilize a method that understands the Subassembly number vs Part number for parenting purposes later
        partLists=[['149269','150710','149816','152881','152585','150705','145135'],['149278','146530','149818'],['149272','149818','146228'],['149270','149820','152395','152395','146445','146445','145133','149683',],['149271','149820','152395','152395','146445','146445']]
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
                        time.sleep(5)
                        parentButton = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[2]/div/button')
                        parentButton.click()
                        time.sleep(5)
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
    unittest.main(verbosity=2)
