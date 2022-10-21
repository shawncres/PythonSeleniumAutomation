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
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Locators_HM import ri_locators






##from azure.identity import DefaultAzureCredential
##from azure.storage.blob import BlobServiceClient

# Acquire a credential object
##credential = DefaultAzureCredential()
##
##blob_service_client = BlobServiceClient(
##        account_url="https://<my_account_name>.blob.core.windows.net",
##        credential=credential)
##
##
##
##
##
options = Options()
options.use_chromium = True



options.add_argument(b'user-data-dir=C:\Users\SHAWNC~1\AppData\Local\Temp\scoped_dir20104_9942196\Default') 

options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

driver = webdriver.Edge(options)
driver.implicitly_wait(10)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


global GUID
GUID = ''
driver.get(ri_locators.ri_page)
