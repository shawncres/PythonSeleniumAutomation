from Locators_HM import ri_locators

def setupRI():
    '''Initiates selenium and pulls up the Robot Identification page'''
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


def setRIN():
    '''Asks for RIN to be used in Ant creation throughout the test'''
    global RIN
    RIN = input('What is the Ants friendly name?: ').strip().upper()
    print(RIN)

def getGUID():
    '''Uses preset RIN to extract the GUID to be used in later parenting logic'''
    global GUID
    driver.get(ri_locators.ri_page)
    time.sleep(3)
    driver.find_element(by = By.XPATH, value=ri_locators.searchbox).send_keys(RIN)
    driver.find_element(by = By.XPATH, value=ri_locators.searchBtn).click()
    time.sleep(3)
    GUID = driver.find_element(by = By.XPATH, value='//*[@id="application"]/div[3]/div/div[1]/div[3]/table/tbody/tr/td[1]').text  
    print(GUID)
