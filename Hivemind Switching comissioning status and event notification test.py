from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import selenium
import random
import warnings



class TestAntCommissionEvent(unittest.TestCase):

    def test_commissioningStatusChangeOn(self):


        driver = webdriver.Edge()
        driver.implicitly_wait(10)

        driver.get("https://attabotics-hivemind-test.azurewebsites.net/")

        driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button').click()
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.ui.inverted.left.vertical.sidebar.menu.overlay.visible > div:nth-child(3) > div.menu > a:nth-child(3)').click()
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > i').click()
        time.sleep(3)





        driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button[4]').click()



        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div:nth-child(3) > div.ui.top.attached.tabular.tiny.menu > a:nth-child(2)').click()

        time.sleep(3)
        ##positive assertion of notification
        self.assertEqual(driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div:nth-child(3) > div.ui.bottom.attached.tab.segment.active > div > div.ui.feed > div:nth-child(1) > div.content > div.extra.text').text, 'In Commission?: No => Yes', 'Failed')



    def test_commissioningStatusChangeOff(self):


        driver = webdriver.Edge()
        driver.implicitly_wait(10)

        driver.get("https://attabotics-hivemind-test.azurewebsites.net/")

        driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[2]/div[1]/button').click()
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.ui.inverted.left.vertical.sidebar.menu.overlay.visible > div:nth-child(3) > div.menu > a:nth-child(3)').click()
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > i').click()
        time.sleep(3)





        driver.find_element(by=By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button[4]').click()



        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div:nth-child(3) > div.ui.top.attached.tabular.tiny.menu > a:nth-child(2)').click()

        time.sleep(3)
        ##positive assertion of notification
        self.assertTrue(driver.find_element(by=By.CSS_SELECTOR, value='#application > div.pusher > div > div:nth-child(1) > div > div > div:nth-child(3) > div.ui.bottom.attached.tab.segment.active > div > div.ui.feed > div:nth-child(1) > div.content > div.extra.text').text == 'In Commission?: Yes => No')









if __name__ == '__main__':
    unittest.main(verbosity=2)



