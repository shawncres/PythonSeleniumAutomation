from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import warnings

class TestAntDetails(unittest.TestCase):

    def test_details_testenv(self):
            driver = webdriver.Edge()

            driver.implicitly_wait(15)
            driver.get("https://attabotics-hivemind-test.azurewebsites.net/")
            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning) 

            ham = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button')
            ham.click()


            time.sleep(3)
            comAnts = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[1]/div[3]/div[2]/a[3]')
            comAnts.click()

            searchAnt = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[1]/div[3]/div/input')
            searchAnt.send_keys('Antioch')

##            sortLastUpdated = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/thead/tr/th[5]/a/span')
##            sortLastUpdated.click()
##            sortLastUpdated.click()

            antDetails = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[1]/td[1]/a/i')
            antDetails.click()


            picksLabel = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]')

            picks = picksLabel.text
            print(picks)

            self.assertTrue(picks in driver.page_source)

    def test_details_prodenv(self):
            driver = webdriver.Edge()

            driver.implicitly_wait(15)
            driver.get("https://attabotics-hivemind.azurewebsites.net/")
            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning) 

            ham = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button')
            ham.click()


            time.sleep(3)
            comAnts = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[1]/div[3]/div[2]/a[3]')
            comAnts.click()

            searchAnt = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[1]/div[3]/div/input')
            searchAnt.send_keys('Antioch')

##            sortLastUpdated = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/thead/tr/th[5]/a/span')
##            sortLastUpdated.click()
##            sortLastUpdated.click()

            antDetails = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div[3]/div/table/tbody/tr[1]/td[1]/a/i')
            antDetails.click()


            picksLabel = driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[2]')

            picks = picksLabel.text
            print(picks)

            self.assertTrue(picks in driver.page_source)


if __name__ == '__main__':
    unittest.main(verbosity=1)

