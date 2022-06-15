from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import selenium
import random
from Locators import ham_locators
##import warnings


driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://attabotics-hivemind-test.azurewebsites.net")
##warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

##Find element syntax driver.find_element(by=By.XPATH, value=ham_locators.ham_menu).click()
