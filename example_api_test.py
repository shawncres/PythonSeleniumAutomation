from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
import time
import unittest
import warnings
import random
import warnings


driver = webdriver.Edge()
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)




driver.get('http://127.0.0.1:8000/about/')



def testing():
    '''Selenium API test, running against a FastAPI uvicorn server from pycharm'''
    try:
        string = "This explains what this api is for "    
        time.sleep(3)
        print(string)
        if string in driver.page_source:
            print('We have a passed test')            
        else:
            print('Test failed')
    except:
        pass 
    driver.close()

if __name__ == '__main__':
    testing()
