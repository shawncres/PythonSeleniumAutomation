from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
import selenium
import random

driver = webdriver.Edge()
driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/parent_serial_number")
time.sleep(3)

partList=['149270','149820','152395','152395','146445','146445','145133','149683']
serialList=['149270-VJ825-617','145133-VJ825-157','149683-VJ825-528']





for i in serialList:
    if serialList[0] != i:
        time.sleep(2)
        snfield1 = driver.find_element_by_xpath('//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[1]/div/input')
        snfield1.send_keys(serialList[0])
        time.sleep(3)
        snfield2 = driver.find_element_by_xpath('//*[@id="application"]/div[3]/div/div[1]/div/div/div[1]/div[2]/div/input')
        snfield2.send_keys(i)
        time.sleep(3)
        parentButton = driver.find_element_by_xpath('//*[@id="application"]/div[3]/div/div[1]/div/div/div[2]/div/button')
        parentButton.click()
        time.sleep(5)
        driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/parent_serial_number")

time.sleep(4)
driver.get("https://attabotics-hivemind-test.azurewebsites.net/manufacturing/assemblies/{0}#hierarchy".format(serialList[0]))

print(serialList[0])
