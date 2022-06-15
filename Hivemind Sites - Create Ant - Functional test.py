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

if __name__ == '__main__':
    unittest.main(verbosity=2)

## copy pasting using action chains
##
##import Action chains
##SyntaxError: invalid syntax
##from selenium.webdriver import ActionChains
##double_click(RIN)
##Traceback (most recent call last):
##  File "<pyshell#30>", line 1, in <module>
##    double_click(RIN)
##NameError: name 'double_click' is not defined
##action =ActionChains(driver)
##action.double_click(RIN).perform()
##action.key_down(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.send_keys('c')
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.key_up(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##
##radioID = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/form/div[4]/div[1]/input')
##radioID.click()
##action.key_down(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.send_keys('v')
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.key_up(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.double_click(RIN).perform()
##action.key_down(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.send_keys('c')
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.key_up(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.perform()
##radioID.click()
##action.key_down(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.send_keys('v')
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.key_up(Keys.CONTROL)
##<selenium.webdriver.common.action_chains.ActionChains object at 0x000001563846D8A0>
##action.perform()
##




##
##
##ham = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button')
##ham.click()
##
##time.sleep(2)
##
##sites = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[1]/div[3]/div[2]/a[1]')
##sites.click()
##
##time.sleep(8)
##vAntsBut = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[1]/td[7]/div/button[1]')
##vAntsBut.click()
##
##time.sleep(4)
##ham = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button')
##ham.click()
##
##time.sleep(2)
##
##sites = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[1]/div[3]/div[2]/a[1]')
##sites.click()
##
##time.sleep(8)
##vWsBut = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[1]/td[7]/div/button[2]')
##vWsBut.click()
##



##time.sleep(2)
##x = driver.find_element(by=By.XPATH, value='')
##x.click()

##
##text = driver.find_element_by_id('textbtn')
##text.click()
##
##awk1 = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[1]/div[3]/div[2]/a[1]')
##awk1.click()
##
##time.sleep(1)
##
##awk2 = driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/p[2]/label')
##awk2.click()
##
##time.sleep(1)
##
##awk3 = driver.find_element(by=By.XPATH, value='/html/body/div[7]/div/p[3]/input')
##
##time.sleep(1)
##
##awk3.click()
##
##time.sleep(2)
##
##chat = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea')
##
##
##
##chat.send_keys('Hello?')
##  
##chat.send_keys(Keys.ENTER)
##
##
##
##



##
##google search
##search = driver.find_element_by_name('q')
##search.send_keys('fuck')
##
##search.send_keys(Keys.RETURN)




##PATH = ("C:\Users\shawn\pyprojsel\Webdriver")
##driver = webdriver.Edge(PATH)
##
##
##options = EdgeOptions()
##driver = webdriver.Edge(options=options)
##
##
##driver.get('http://google.com")
##
##
##driver.quit()
##
##
##









##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##import time
##
##
##PATH = "C:\Users\shawn\pyprojsel\Webdriver\msedgedriver.exe"
##driver = webdriver.Edge(PATH)
##
##driver.get("https://stangricki.github.io/Website-Mizuxe/index.html")
##print(driver.title)
##
##print(driver.get_cookie)
##
##search = driver.find_element_by_id('newsletter')
##
##search.send_keys("standard_user")
##search.send_keys(Keys.RETURN)
