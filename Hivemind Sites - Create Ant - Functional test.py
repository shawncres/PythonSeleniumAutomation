from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import warnings
import random

driver = webdriver.Edge()
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


class TestAntCreation(unittest.TestCase):

    def test_create(self):
            # NOTE: URL sanitized for public repository
            driver.get("https://<company>-hivemind-test.example.com/")
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
            antassemblypage= 'https://<company>-hivemind-test.example.com/manufacturing/assemblies/'+GUID+'#heirarchy'

            driver.get('{0}'.format(antassemblypage))

                
            time.sleep(6)
                        
            if GUID in driver.page_source:
                print('Ant created successfully GUID is {0}'.format(GUID))
            else:
                print('Ant not found')
            self.assertTrue(GUID in driver.page_source)

            driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)