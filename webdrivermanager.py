
## Set up Script that invokes Edge Using Webdriver, the manager should manage updates
## to Coincide with the Edge browser being updated.
## Import this module and declare the driver as one of these functions, after that you can use all the driver functions as expected 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import unittest
import warnings
import random
import warnings
import qrcode


def startEdgeDriver():
    '''Declare the driver variable as this function after importing this module for Edge  '''  
    from selenium import webdriver
    from selenium.webdriver.edge.service import Service as EdgeService
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    
    return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))



def startChromeDriver():
    '''Declare the driver variable as this function after importing this module for Chrome  '''    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

## Must add driver as argument     
def screenshot(driver):
    time.sleep(3)
    filename = (str(time.ctime())+'.png').replace(' ','_').replace(':', '')                                                               
    path = r'C:\Users\ShawnCooper\pyproj\automationtests\Atta\Screenshots\{}'.format(filename)                                                               
    driver.save_screenshot(path)
    time.sleep(3)
    print(f'Screenshot captured as {filename}')
 


if __name__=='__main__':
##    startChromeDriver('https://www.google.com/')
    startEdgeDriver()

    
    
